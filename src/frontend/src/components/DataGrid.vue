<template>
  <div id="example1">
    <hot-table :settings="settings">
    </hot-table>
    <b-button @click="check">CHECK</b-button>
    <b-button @click="insertElem">Submit</b-button>
  </div>
</template>

<script>
import { HotTable } from "@handsontable/vue";
// import Handsontable from "handsontable";
import axios from "axios";

export default {
  components: {
    HotTable,
    // HotColumn
  },
  data() {
    return {
      items : [],
      settings: {
        data: [],
        colHeaders: ['Part Number', 'Item Type', 'PARENT', 'Q/ASSY'],
        stretchH: 'all',
        minSpareRows: 1,
        colWidths: 300,
        columns: [
          {
            data: 'part_number'
            // 1nd column is simple text, no special options here
          },
          {
            data: 'tipo',
          },
          {
            data: 'parent',
            type: 'numeric',
            allowEmpty: false
          },
          {
            data: 'qty',
            type: 'numeric',
            allowEmpty: false
          },
        ],
        width: '100%',
        rowHeights: 40,
        rowHeaders: true,
        licenseKey: "non-commercial-and-evaluation",
        className: "htMiddle htCenter",
        contextMenu: [
          'row_above',
          'row_below',
          '---------',
          'remove_row',
          '---------',
          'undo',
          'redo',
          '---------',
          'make_read_only',
          '---------',
          'alignment',
          '---------',
          'copy',
          'cut',
        ]
      }
    };
  },
  methods: {
    check(){
      console.log(this.settings.data)
    },
    getData() {
      let items = []

      for (let i = 1; i <= this.$route.params.items_number; i++) {
        // this.settings.data.push([100 * i,'MAT', null, 1])
        // items.push({part_number: 100 * i, tipo: 'MAT', parent: null, qty: 1})
        // this.items.push([100 * i, 'MAT', null, 1])
      }
      return items
    },
    insertElem() {
      for(let row=0; row<this.settings.data.length; row++) {
        this.items.push({
          part_number: this.settings.data[row][0],
          tipo: this.settings.data[row][1],
          parent: this.settings.data[row][2],
          qty: this.settings.data[row][3]
        })
      }

      for(let i=0; i<this.items.length; i++) {
        axios.post("http://localhost:8000/api/v1.0/items/", this.items[i]).then((response) => {
        console.log(response.data)
        })
        .catch((error) => {
          console.log(error)
        })
      }
    }
  },
  created() {
    for (let i = 1; i <= this.$route.params.items_number; i++) {
      this.settings.data.push({part_number: 100 * i, tipo: 'MAT', parent: null, qty: 1})
    }
  },
  mounted() {
    
  }
};
</script>

<style>
@import "~handsontable/dist/handsontable.full.css";
</style>