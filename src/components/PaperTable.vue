<template>
  <table  class="table" :class="tableClass">
    <thead>
    <slot name="columns">
      <th v-for="column in columns" :key="column">{{column}}</th>
    </slot>
    </thead>
    <tbody>
    <tr v-for="(item, index) in data" :key="index">
      <slot :row="item">
        <td v-for="(column, idx) in columns" 
            :key="idx" >
            <a v-if="column==`id`">{{index}}</a>
            <a v-else @click="">
            {{itemValue(item, column)}}
            </a>
        </td>
      </slot>
      <button @click="deleteTicker(item)" >delete</button>
    </tr>
    </tbody>
  </table>
</template>
<script>
import EventBus from "@/plugins/EventBus"
export default {
  name: 'paper-table',
  props: {
    columns: Array,
    data: Array,
    type: {
      type: String, // striped | hover
      default: "striped"
    },
    title: {
      type: String,
      default: ""
    },
    subTitle: {
      type: String,
      default: ""
    }
  },
  created() {
    this.clickTable()
  },
  computed: {
    tableClass() {
      return `table-${this.type}`;
    }
  },
  methods: {
    hasValue(item, column) {
      return item[column.toLowerCase()] !== "undefined";
    },
    itemValue(item, column) {
      return item[column];
    },
    deleteTicker(item){
      this.$parent.$parent.deleteTickerfrom(item)

    },
    clickTable(){
      EventBus.$emit("table-click","this is the message")
    }
  }
};
</script>
<style>
</style>
