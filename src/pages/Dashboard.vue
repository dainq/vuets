<template>
  <div>
    <!--input ticker cards-->

    <form>
      <label for="fname">Input ticker </label>
      <input v-model="ticker" type="text" id="fname" name="fname" /><br /><br />
      <p>{{ tickerFullName }}</p>
      <button type="button" @click="getTickerData">Search</button>
    </form>
    <!--Charts-->
    <CandleStick :option="option"/>
    <ul>
      <p>list</p>
      <li v-for="record in tickerData" :key="record.Date">
        {{ record.PriceOpen }}
        {{ record.PriceClose }}
        {{ record.PriceLow }}
        {{ record.PriceHigh }}
      </li>
    </ul> -->
    <div>{{option}}</div>
  </div>
</template>
<script>
import axios from "axios";
import { StatsCard, ChartCard, Button } from "@/components/index";
import Pie from "./chart/Pie.vue";
import CandleStick from "./chart/CandleStick.vue";
import Pie2 from "./chart/Pie2.vue";
function processData(rawData) {
  console.log("processData");
  console.log(rawData);
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
    xAxis: {
      data:xAxis
    },
    yAxis: {},
    series: [
      {
        type: "candlestick",
        data: data,
      },
    ],
  };
}
export default {
  components: {
    Button,
    Pie,
    StatsCard,
    ChartCard,
    CandleStick,
    Pie2,
  },
  /**
   * Chart data used to render stats, charts. Should be replaced with server data
   *c
   */
  data() {
    return {
      ticker: "VIC",
      tickerFullName: "",
      tickerData: [],
      option: {},
    };
  },
  methods: {
    searchTicker() {
      return None;
    },
    getTickerData() {
      const instance = axios.create({
        withCredentials: true,
        baseURL:
          "https://www.fireant.vn/api/Data/Companies/HistoricalQuotes?symbol=API&startDate=2021-12-12&endDate=2022-1-12",
      });
      const res = instance
        .get(
          `https://www.fireant.vn/api/Data/Companies/HistoricalQuotes?symbol=${this.ticker}&startDate=2021-12-12&endDate=2022-1-12`,
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
          this.tickerData = response.data;
          this.option = processData(this.tickerData);
          console.log(this.option)
        });
    },
  },
};
</script>
<style></style>
</style>
