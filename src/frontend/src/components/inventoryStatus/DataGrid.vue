<template>
  <div>
    <label class="title">Inventory Status: {{ invFile.title }}</label>
    <hot-table :settings="settings"></hot-table>
  </div>
</template>

<script>
import store from "@/store";
import { HotTable } from "@handsontable/vue";
import { mapGetters, mapActions, mapState } from "vuex";
import Handsontable from "handsontable";

export default {
  name: "InventoryStatus",
  store,
  components: {
    HotTable
    // HotColumn
  },
  data() {
    return {
      hotRef: null,
      settings: {
        data: [],
        colHeaders: ["Part Number", "Safe Stock", "On Hand", "Past Due"],
        stretchH: "all",
        colWidths: 50,
        afterChange: changes => {
          if (changes) {
            changes.forEach(([row, prop, oldValue, newValue]) => {
              prop;
              oldValue;
              if (newValue && newValue.trim() != "") {
                // Obteniendo todos los keys que empiecen con receipt
                let keys = Object.keys(this.settings.data[row]).filter(
                  key => key.startsWith("receipt") && key != "receipts"
                );
                // Guardando todos los receipts en la propiedad receipts
                this.settings.data[row].receipts = keys
                  .map(key => this.settings.data[row][key])
                  .join(",");

                this.updateInvItem(this.settings.data[row]);
              }
            });
          }
        },
        beforeRemoveRow: (_, amount, physicalRows) => {
          console.log(amount)

          physicalRows.forEach(index => {
            this.deleteInvItem(this.settings.data[index]);
          })
        },
        columns: [
          {
            data: "part_number",
            validator: function(value, callback) {
              if (!value || value.trim() == "") callback(false);
              else callback(true);
            }
          },
          {
            data: "safe_stock",
            validator: /[0-9]+$/
          },
          {
            data: "on_hand",
            validator: /[0-9]+$/
          },
          {
            data: "past_due",
            validator: /[0-9]+$/
          }
        ],
        undo: true,
        rowHeights: 40,
        rowHeaders: true,
        licenseKey: "non-commercial-and-evaluation",
        className: "htMiddle htCenter",
        contextMenu: true,
        manualColumnResize: true,
        manualRowResize: true
      }
    };
  },
  computed: {
    ...mapGetters(["getAllInvItems", "getAllInvItems", "invFile"]),
    ...mapState({
      inv_files: state => state.invFile
    }),
    countReceipts() {
      return this.settings.data[0].receipts.split(",").length;
    }
  },

  created() {
    this.fetchInvFile(this.$route.params.file);

    this.$store.subscribe(mutation => {
      if (mutation.type === "setInvItems") {
        for (
          let i = 1;
          i <= Object.keys(this.getAllInvItems[0]).length - 7;
          i++
        ) {
          this.settings.colHeaders.push("Receipt " + i);
          this.settings.columns.push({
            data: "receipt" + i,
            validator: /[0-9]+$/
          });
        }

        this.settings.data = this.getAllInvItems;
      }

      this.settings.contextMenu = {
        items: {
          add_column: {
            name: "Add receipt column",
            callback: this.addColumn
          },
          remove_column: {
            name: function() {
              let colFrom = this.getSelectedRangeLast().from.col
              let colTo = this.getSelectedRangeLast().to.col
              if(colFrom === colTo) {
                return "Remove receipt column"
              } else {
                return "Remove receipts columns"
              }
            },
            callback: this.removeColumn,
            disabled: function() {
              // Disable option when first, second, third and fourth row were clicked
              return (
                this.getSelectedLast()[1] === 0 ||
                this.getSelectedLast()[1] === 1 ||
                this.getSelectedLast()[1] === 2 ||
                this.getSelectedLast()[1] === 3
              ); // `this` === hot3
            }
          },
          "---------": {},
          add_row: {
            name: "Add row bottom",
            callback: this.addRow
          },
          remove_row: {},
          separator: Handsontable.plugins.ContextMenu.SEPARATOR,
          copy: {},
          cut: {}
        }
      };

      if (mutation.type === "updatedInvItem") {
        this.$bvToast.show("saved-toast");
      } else if(mutation.typ === "deletedInvItem") {
        this.$bvToast.show("saved-toast");
      }
    });
  },
  watch: {
    invFile() {
      this.fetchInvItems(this.$route.params.file);
    }
  },
  methods: {
    ...mapActions([
      "fetchInvFile",
      "fetchInvItems",
      "updateInvItem",
      "deleteInvItem",
      "addInvItem"
    ]),
    check() {
      console.log(this.settings.data);
    },
    addColumn() {
      this.settings.colHeaders.push(`Receipt  ${this.countReceipts + 1}`);
      this.settings.columns.push({
        data: `receipt${this.countReceipts + 1}`,
        validator: /[0-9]+$/
      });

      this.settings.data.forEach(item => {
        item.receipts += ",0";
        this.updateInvItem(item);
      });
    },
    removeColumn(key, selection) {
      key
      console.log(selection)
      let colStart = selection[0].start.col - 4;
      let colEnd = selection[0].end.col - 4;
      let colsQty = colEnd - colStart + 1

      this.settings.data.forEach(elem => {
        let rec = elem.receipts.split(",")
        rec.splice(colStart, colsQty)
        elem.receipts = rec.join(",")
        this.updateInvItem(elem)
      })

      this.settings.colHeaders.splice(-colsQty, colsQty);
      this.settings.columns.splice(-colsQty, colsQty);
    },
    addRow() {
      const item = {
        part_number: null,
        safe_stock: 0,
        on_hand: 0,
        past_due: 0,
        receipts: "0",
        file: this.invFile.id
      }

      this.addInvItem(item);
    }
  }
};
</script>

<style scoped>
@import "~handsontable/dist/handsontable.full.css";

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