<template>
  <div>
    <v-chart class="chart" :option="candlestick" />
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
import VChart, { THEME_KEY } from "vue-echarts";
import {
  TitleComponent,
  TooltipComponent,
  LegendComponent,
} from "echarts/components";
import { GridComponent } from "echarts/components";

use([
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

  data() {
    return {
      candlestick:this.option ,
    };
  },
};
</script>
