<template>
  <div>
    <!-- <hot-table id="hottable" :settings="settings"></hot-table> -->
    <div id="tablita"></div>
  </div>
</template>

<script>
// import { HotTable } from "@handsontable/vue";
import Handsontable from "handsontable";
export default {
  components: {
    // HotTable
  },
  data() {
    return {
      hotRef: null,
      settings: {
        data: [
			["544", "2t4"]
		],
        colHeaders: ["Part Number", "Parent", "QTY"],
        stretchH: "all",
        colWidths: 100,
        afterChange: changes => {
          if (changes) {
            changes.forEach(([row, prop, oldValue, newValue]) => {
              row;
              oldValue;
              newValue;
              console.log(prop);
            });
          }
        },
        cells: function(row, column, prop) {
          const cellProperties = {};
          const visualRowIndex = this.instance.toVisualRow(row);
          const visualColIndex = this.instance.toVisualColumn(column);

          if (visualRowIndex === 0 && visualColIndex === 0) {
            cellProperties.readOnly = true;
          }

          return cellProperties;
        },

        rowHeights: 40,
        rowHeaders: true,
        licenseKey: "non-commercial-and-evaluation",
        className: "htMiddle htCenter"
      }
    };
  },
  methods: {
    // 	  this.setCellMetaObject = function(row, column, prop) {
    //     if (typeof prop === 'object') {
    //       objectEach(prop, (value, key) => {
    //         this.setCellMeta(row, column, key, value);
    //       });
    //     }
    //   };
  },
  mounted() {
    const container1 = document.getElementById("tablita");
    this.hotRef = new Handsontable(container1, this.settings);

    this.hotRef.setDataAtCell(0, 1, "Ford");
    this.hotRef.setCellMetaObject(0, 0, { part_number: "90" });
  }
};
</script>

<style>
</style>
