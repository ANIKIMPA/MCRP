<template>
  <div id="example1">
    <label class="title">Bill of Material: {{ bomFile.title }}</label>
    <hot-table :settings="settings"></hot-table>
  </div>
</template>

<script>
import { HotTable } from "@handsontable/vue";
import { mapActions, mapGetters } from "vuex";

export default {
  name: "BillOfMaterial",
  components: {
    HotTable
    // HotColumn
  },
  data() {
    return {
      settings: {
        data: [],
        colHeaders: ["Part Number", "Item Type", "Q/ASSY", "PARENT"],
        stretchH: "all",
        colWidths: 300,
        afterChange: changes => {
          if (changes) {
            changes.forEach(([row, prop, oldValue, newValue]) => {
              prop
              oldValue
              if(newValue && newValue.trim() != "") {
                this.updateBomItem(this.settings.data[row]);
              }
            });
          }
        },
        columns: [
          {
            data: "part_number",
            validator: function(value, callback) {
              if(!value || value.trim() == "")
                callback(false)
              else
                callback(true)
            }
          },
          {
            data: "tipo",
            allowEmpty: false
          },
          {
            data: "qty",
            validator: /[0-9]+$/
          }
        ],
        beforeRemoveRow: (_, amount, physicalRows) => {
          console.log(amount)

          physicalRows.forEach(index => {
            this.deleteBomItem(this.settings.data[index]);
          })
        },
        rowHeights: 40,
        rowHeaders: true,
        licenseKey: "non-commercial-and-evaluation",
        className: "htMiddle htCenter",
        contextMenu: {
            items: {
              add_row: {
              name: "Add row bottom",
              callback: this.addRow
            },
            remove_row: {},
            "---------": {},
            undo: {},
            redo: {},
            copy: {},
            cut: {}
          }
        }
      }
    };
  },
  methods: {
    ...mapActions(["updateBomItem", "addBomItem", "fetchBomFile", "fetchBomItems", "deleteBomItem"]),
    addRow() {
      this.addBomItem({
        part_number: null,
        tipo: "MAT",
        parent: null,
        qty: 1,
        file: this.$route.params.file
      });
      this.$bvToast.show("saved-toast");
    }
  },
  computed: {
    ...mapGetters(["getAllBomItems", "bomFile"]),
    allPartNumbers() {
      let part_numbers = [];

      for (let i = 0; i < this.getAllBomItems.length; i++) {
        part_numbers.push(this.getAllBomItems[i].part_number);
      }

      return part_numbers;
    }
  },
  created: function() {
    this.fetchBomFile(this.$route.params.file);
    this.fetchBomItems(this.$route.params.file);

    this.$store.subscribe(mutation => {
      if (mutation.type === "setBomItems") {
        this.settings.columns.push({
          data: "parent",
          type: 'dropdown',
          source: this.allPartNumbers
        });
        this.settings.data = this.getAllBomItems;
      } else if(mutation.type === "updateBomItem") {
        this.$bvToast.show("saved-toast");
        this.settings.columns[3] = ({
          data: "parent",
          type: 'dropdown',
          allowEmpty: true,
          source: this.allPartNumbers
        });
      } else if (mutation.type === "deletedBomItem") {
        this.$bvToast.show("saved-toast");
      }
    });
  }
};
</script>

<style scoped>
@import "~handsontable/dist/handsontable.full.css";

.handsontable.listbox td.htDimmed {
  background-color: #eceff1;
  padding: 8px;
  box-shadow: 10px;
}
.handsontable.listbox td.htDimmed:hover {
  /* background-color: #5292F7; */
  background-color: #bbdefb;
}

.handsontable.listbox tr td.current, .handsontable.listbox tr:hover td {
    background: #babdbe
}

.title {
  position: absolute;
  top: 16px;
  color: #ffffff;
  z-index: 200;
  left: 50%;
  width: 600px;
  margin-left: -300px;
}
</style>
