<template>
  <div>
    <!--input ticker cards-->

    <label for="fname">Input ticker </label>
    <input
      v-model="ticker"
      @keyup.enter="getTickerData"
      type="text"
      id="fname"
      name="fname"
      onclick="this.select()"
    /><br /><br />
    <button @click="addTickertoPortfolio()">Add this ticker to portfolio</button>
    <p>Select portfolio</p>
    <select v-model="PortfolioName">
            <option selected disabled value="" >Portfolio</option>
            <option v-for="l in PortfolioList"  :key="l.id">
                {{ l }}
            </option>
    </select>
    <!--Charts-->
    <TableList :PortfolioName="PortfolioName" ref="TableList"/>
    <CandleStick :option="option" />


    <div>{{ option }}</div>
  </div>
</template>
<script>
import EventBus from "@/plugins/EventBus"
import axios from "axios";
import { StatsCard, ChartCard, Button } from "@/components/index";
import TableList from '@/pages/TableList';
import CandleStick from "./chart/CandleStick.vue";

var today = new Date();
var todayString =
  today.getFullYear() + "-" + today.getMonth() + 1 + "-" + today.getDate();

var listPortfolio = ["A","B","C","D","E","F","G","H"]

function calculateMA(dayCount,data) {
  var result = [];
  for (var i = 0, len = data.values.length; i < len; i++) {
    if (i < dayCount) {
      result.push('-');
      continue;
    }
    var sum = 0;
    for (var j = 0; j < dayCount; j++) {
      sum += +data.values[i - j][1];
    }
    result.push(sum / dayCount);
  }
  return result;
}
function processData(rawData,ticker) {
  console.log("processData");
  let xAxis = [];
  let yAxis = [];
  let data = [];
  for (var record in rawData) {
    xAxis.push(rawData[record].Date);
    data.push([
      rawData[record].PriceOpen,
      rawData[record].PriceClose,
      rawData[record].PriceLow,
      rawData[record].PriceHigh,
    ]);
  }
  console.log(xAxis);
  return {
  title: {
    text: ticker,
    left: 0
  },
  tooltip: {
    trigger: 'axis',
    axisPointer: {
      type: 'cross'
    }
  },
  legend: {
    data: ['View']
  },
  grid: {
    left: '10%',
    right: '10%',
    bottom: '15%'
  },
  xAxis: {
    type: 'category',
    data: xAxis,
    scale: true,
    boundaryGap: false,
    axisLine: { onZero: false },
    splitLine: { show: false },
    min: 'dataMin',
    max: 'dataMax'
  },
  yAxis: {
    scale: true,
    splitArea: {
      show: true
    }
  },
  dataZoom: [
    {
      type: 'inside',
      start: 50,
      end: 100
    },
    {
      show: true,
      type: 'slider',
      top: '90%',
      start: 50,
      end: 100
    }
  ],
  series: [
    {
      name: 'View',
      type: 'candlestick',
      data: data,
      markPoint: {
        label: {
          formatter: function (param) {
            return param != null ? Math.round(param.value) + '' : '';
          }
        },
        data: [
          {
            name: 'Mark',
            coord: ['2013/5/31', 2300],
            value: 2300,
            itemStyle: {
              color: 'rgb(41,60,85)'
            }
          },
          {
            name: 'highest value',
            type: 'max',
            valueDim: 'highest'
          },
          {
            name: 'lowest value',
            type: 'min',
            valueDim: 'lowest'
          },
          {
            name: 'average value on close',
            type: 'average',
            valueDim: 'close'
          }
        ],
        tooltip: {
          formatter: function (param) {
            return param.name + '<br>' + (param.data.coord || '');
          }
        }
      },
      markLine: {
        symbol: ['none', 'none'],
        data: [
          [
            {
              name: 'from lowest to highest',
              type: 'min',
              valueDim: 'lowest',
              symbol: 'circle',
              symbolSize: 10,
              label: {
                show: false
              },
              emphasis: {
                label: {
                  show: false
                }
              }
            },
            {
              type: 'max',
              valueDim: 'highest',
              symbol: 'circle',
              symbolSize: 10,
              label: {
                show: false
              },
              emphasis: {
                label: {
                  show: false
                }
              }
            }
          ],
          {
            name: 'min line on close',
            type: 'min',
            valueDim: 'close'
          },
          {
            name: 'max line on close',
            type: 'max',
            valueDim: 'close'
          }
        ]
      }
    },
    {
      name: 'MA5',
      type: 'line',
      data: calculateMA(5,data),
      smooth: true,
      lineStyle: {
        opacity: 0.5
      }}
      ]
  }
};

export default {
  components: {
    Button,
    StatsCard,
    ChartCard,
    CandleStick,
    TableList
  },
  /**
   * Chart data used to render stats, charts. Should be replaced with server data
   *c
   */
  data() {
    return {
      ticker: "Vnindex",
      tickerFullName: "",
      tickerData: [],
      option: {},
      PortfolioList: listPortfolio,
      PortfolioName: "A",
    };
  },
  created() {
     // Listening the event hello
    EventBus.$on('table-click', this.tableClickHander);
    
  },
  compute: {
  },
  methods: {
    searchTicker() {
      return None;
    },
    validateTicker(){

    },
    isTickerExist(tickerdata){
    return this.tickerData.length == 0



    },
    isTickerinPortfolio(ticker,portfolio){
      axios.get(`http://localhost:3000/${portfolio}/`).then((response) => {
        const tickerlist = response.data.map(element => element["TickerName"])
        console.log(tickerlist.includes(ticker))
        if (tickerlist.includes(ticker)){
          return true;
        }else{
          return false;
        }

      });
      

    },
    getTickerData() {
      const instance = axios.create({
        withCredentials: true,
        baseURL:
          "https://www.fireant.vn/api/Data/Companies/HistoricalQuotes?symbol=API&startDate=2021-12-12&endDate=2022-1-12",
      });
      const res = instance
        .get(
          `https://www.fireant.vn/api/Data/Companies/HistoricalQuotes?symbol=${this.ticker}&startDate=2021-01-12&endDate=${todayString}`,
          {
            Connection: "keep-alive",
            "sec-ch-ua":
              '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
            Accept: "application/json, text/plain, */*",
            RequestVerificationToken:
              "9eD6cKrE0rKSK7MNskVjmTQiRjUc3Bkuu8l2g4nFqJJX3aub9jmE0fFWD1jdZuXBQ9IuTgBZeWv7xFM9bhv1YzO6euE1:4KKx5oM7iwxQf67oa0lJsrqSWbIrBd8_wu-Ru6NcpfUhMD0iCzILMxBCc9yZWGA8zIw96-UjBgsZXwAf-wj_qOMy5pA1",
            "sec-ch-ua-mobile": "?0",
            "User-Agent":
              "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
            "sec-ch-ua-platform": '"Windows"',
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            Referer: "https://www.fireant.vn/Home/StockDetail/API",
            "Accept-Language": "ja,en-US;q=0.9,en;q=0.8",
            Cookie:
              "ASP.NET_SessionId=luubf2lplsuqig5pbmv0s1ib; _ga=GA1.2.849319539.1641982875; _gid=GA1.2.430608104.1641982875; _gat=1",
          }
        )
        .then((response) => {
          console.log("set data");
          this.tickerData = response.data
          if (this.isTickerExist(this.tickerData)) {
            alert("ticker not found");
          } else{
          this.option = processData(this.tickerData,this.ticker);
          console.log(this.option);
          }

        });
    },
    onEnter() {
      console.log("onEnter");
    },
    addTickertoPortfolio() {
      if (this.isTickerExist(this.ticker)){
        alert("Ticker not exists ")

      } else if (this.isTickerinPortfolio(this.ticker,this.PortfolioName)){
        alert("Ticker already in portfolio ")
      }else{
      this.$refs.TableList.addTickertoPortfolio(this.ticker,this.PortfolioName)

      }

      //query data from database get ticker list
    },
    tableClickHander(ticker){
      console.log(`event from paperlist ${ticker}`)
      // this.ticker = ticker
      // this.getTickerData
    }
  },
};
</script>
<style></style>
</style>
