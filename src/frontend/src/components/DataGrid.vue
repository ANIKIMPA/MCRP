<template>
  <div id="example1">
    <hot-table :settings="settings" width="800">
      <hot-column title="Part Number" width="100">
      </hot-column>
      <hot-column :settings="secondColumnSettings" width="100">
      </hot-column>
      <div v-for="n in descendants" :key="'col' + n">
      <hot-column :title="'DESC ' + n" width="100"></hot-column>
      <hot-column :title="'Q/ASSY ' + n" width="100"></hot-column>
      </div>
    </hot-table>
    <b-button @click="check">CHECK</b-button>

    <p>title: {{ $route.params.title }}</p>
    <p># Items: {{ $route.params.items_number }}</p>
    <p>Descendants: {{ $route.params.max_descendants }}</p>
  </div>
</template>

<script>
import { HotTable, HotColumn } from "@handsontable/vue";
import Handsontable from "handsontable";

export default {
  components: {
    HotTable,
    HotColumn
  },
  data() {
    return {
      data: Handsontable.helper.createSpreadsheetData(2, 5),
      secondColumnSettings: {
        title: "Item Type"
      },
      descendants: 0,
      settings: {
        data: [],
        colHeaders: true,
        rowHeaders: true,
        licenseKey: "non-commercial-and-evaluation",
        contextMenu: {
          items: {
            col_left: { },
            col_right: {},
            remove_col: {},
            row_above: {
              name: "Insert row above"
            },
            row_below: {},
            remove_row: {},
            separator: Handsontable.plugins.ContextMenu.SEPARATOR,
            clear_custom: {
              name: "Clear all cells",
              callback: function() {
                this.clear();
              }
            }
          }
        }
      }
    };
  },
  methods: {
    check(){
      console.log(this.settings.data)
    }
  },
  created() {
    this.descendants = this.$route.params.max_descendants * 1
  },
  mounted() {
    for (let i = 1; i <= this.$route.params.items_number; i++) {
      this.settings.data.push([100 * i,'MAT'])
    }
    for (let row = 0; row < this.settings.data.length; row++) {
      for(let desc = 0; desc < this.descendants * 2; desc++) {
        this.settings.data[row].push(null);
      }
    }
  },
  watch: {
  }
};
</script>

<style>
@import "~handsontable/dist/handsontable.full.css";
</style>