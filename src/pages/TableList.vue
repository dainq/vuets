<template>
  <div class="row">
    <div class="col-12">
      <card :title="table1.title" :subTitle="table1.subTitle">
        <div slot="raw-content" class="table-responsive">
          <paper-table v-if="hasValue" :data="table1.data" :columns="table1.columns">
          </paper-table>
        </div>
      </card>
    </div>
  </div>
</template>
<script>
import axios from "axios";
import uuid from "uuid/4"
import { PaperTable } from "@/components";
export default {
  components: {
    PaperTable,
  },
  props: {
    PortfolioName: String,
    TickertoAdd: String
  },
  watch: {
    PortfolioName:function(newValue){
      this.getPortfolioTicker(newValue)
    },
    TickertoAdd: function(newValue){
      this.addTickertoPortfolio(newValue,this.PortfolioName)

    }

    
  },
  computed: {
    hasValue:function(){
      return this.PortfolioData["tableData"].length

    },
  },
  created() {
    console.log(this.PortfolioName);
    this.getPortfolioTicker("A");
  },
  data() {
    return {
      PortfolioData: {
        "tableColumns":[],
        "tableData": {},

      },
      table1: {}
    };
  },
  methods: {
    getPortfolioTicker(Portfolio) {
      axios.get(`http://localhost:3000/${Portfolio}/`).then((response) => {
        this.processData(response.data);
      });
    },
    processData(data) {
      if (data.length>0){
      this.PortfolioData["tableData"] = data;
      this.PortfolioData["tableColumns"] = Object.keys(data[0]);
      this.table1 = {
        title: "Name Portfolio",
        subTitle: "Here is a subtitle for this table",
        columns: this.PortfolioData["tableColumns"],
        data: this.PortfolioData["tableData"],
      } }
      else{
        this.PortfolioData["tableData"]={}
        this.PortfolioData["tableColumns"] = []
      }
    },
    reload(){
      this.getPortfolioTicker(this.PortfolioName)
    },
    deleteTickerfrom(item){
      var id = item["id"]
      axios
        .delete(`http://localhost:3000/${this.PortfolioName}/${id}`).then(this.reload())
    },
    addTickertoPortfolio(ticker,portfolio){
      const id = uuid()
      console.log(id)
      axios.put(`http://localhost:3000/${this.id}`, ).then(this.reload())
    }}
}
</script>
<style>
</style>
