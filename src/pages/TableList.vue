<template>
  <div class="row">
    <div class="col-12">
      <card :title="table1.title" :subTitle="table1.subTitle">
        <div slot="raw-content" class="table-responsive">
          <paper-table :data="table1.data" :columns="table1.columns">
          </paper-table>
        </div>
      </card>
    </div>
  </div>
</template>
<script>
import axios from "axios";
import { PaperTable } from "@/components";
export default {
  components: {
    PaperTable,
  },
  props: {
    PortfolioName: String,
  },
  watch: {
    PortfolioName:function(newValue){
      this.getPortfolioTicker(newValue)


    }
    
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
      this.PortfolioData["tableData"] = data;
      this.PortfolioData["tableColumns"] = Object.keys(data[0]);
      this.table1 = {
        title: "Name Portfolio",
        subTitle: "Here is a subtitle for this table",
        columns: this.PortfolioData["tableColumns"],
        data: this.PortfolioData["tableData"],
      },
      console.log(this.PortfolioData);
    },
    deleteTicker(ticker){

    }
  },
};
</script>
<style>
</style>
