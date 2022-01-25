<template>
  <div>

    <v-chart class="chart" :option="option" />

  </div>
</template>
<style scoped>
.chart {
  height: 100vh;
}
</style>

<style>
body {
  margin: 0;
}
</style>
<script>
import { use } from "echarts/core";
import { CandlestickChart } from "echarts/charts";
import { CanvasRenderer } from "echarts/renderers";
import { DataZoomComponent } from 'echarts/components';
import VChart, { THEME_KEY } from "vue-echarts";
import {
  TitleComponent,
  TooltipComponent,
  LegendComponent,
} from "echarts/components";
import { GridComponent } from "echarts/components";

use([DataZoomComponent ,
  GridComponent,
  CanvasRenderer,
  CandlestickChart,
  TitleComponent,
  TooltipComponent,
  LegendComponent,
]);

import "echarts/lib/chart/pie";

export default {
  name: "candlestick",
  components: {
    VChart,
  },
  props: {
    option: Object,
  },
  watch: {
    candlestick:function(){
      console.log("propchange")
    }
  },



  data() {
    return {
    };
  },
};
</script>
