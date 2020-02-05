<template>
  <div id="example1">
    <hot-table :settings="settings">
    </hot-table>
    <b-button @click="check">CHECK</b-button>
  </div>
</template>

<script>
import { HotTable } from "@handsontable/vue";
import Handsontable from "handsontable";

export default {
  components: {
    HotTable,
    // HotColumn
  },
  data() {
    return {
      descendants: 0,
      settings: {
        data: [],
        colHeaders: ['Part Number', 'Item Type'],
        colWidths: 100,
        rowHeaders: true,
        licenseKey: "non-commercial-and-evaluation",
        contextMenu: {
          items: {
            col_left: {
            },
            col_right: {},
            remove_col: {},
            separator: Handsontable.plugins.ContextMenu.SEPARATOR,
            row_above: {
              name: "Insert row above"
            },
            row_below: {},
            remove_row: {},
            clear_custom: {
              name: "Clear all cells",
              callback: function() {
                this.clear();
              }
            },
            add_cols: {
              name: "Add new column",
              callback: function() {
                console.log(this)
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
      this.settings.colHeaders.push('DESC ' + 4,'Q/ASSY ' + 4)
    }
  },
  created() {
    this.descendants = this.$route.params.max_descendants * 1
  },
  mounted() {
    for(let n=1; n<= this.descendants; n++) {
      this.settings.colHeaders.push('DESC ' + n,'Q/ASSY ' + n)
    }
    for (let i = 1; i <= this.$route.params.items_number; i++) {
      this.settings.data.push([100 * i,'MAT'])
    }
    for (let row = 0; row < this.settings.data.length; row++) {
      for(let desc = 0; desc < this.descendants * 2; desc++) {
        this.settings.data[row].push(null);
      }
    }
  }
};
</script>

<style>
@import "~handsontable/dist/handsontable.full.css";
</style>