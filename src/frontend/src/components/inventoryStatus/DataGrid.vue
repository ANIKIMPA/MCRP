<template>
  <div>
    <label class="title">Inventory Status: {{ invFile.title }}</label>
    <hot-table :settings="settings"></hot-table>
  </div>
</template>

<script>
import store from "@/store";
import { HotTable } from "@handsontable/vue";
import { mapGetters, mapActions, mapMutations } from "vuex";
import Handsontable from "handsontable";
import validator from "@/js/validator";

export default {
  name: "InventoryStatus",
  store,
  components: {
    HotTable
  },
  data() {
    return {
      settings: {
        data: [],
        colHeaders: ["Part Number", "Safe Stock", "On Hand", "Past Due"],
        stretchH: "all",
        colWidths: 50,
        afterChange: changes => {
          if (changes) {
            changes.forEach(([row, prop, oldValue, newValue]) => {
              if (this.isValidReceipt({ row, prop, oldValue, newValue })) {
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
          amount;

          physicalRows.forEach(index => {
            this.deleteInvItem(this.settings.data[index]);
          });
        },
        columns: [
          {
            data: "part_number",
            validator: (value, callback) =>
              callback(validator.isNotEmpty(value))
          },
          {
            data: "safe_stock",
            type: "numeric",
            validator: (value, callback) =>
              callback(validator.isPositive(value))
          },
          {
            data: "on_hand",
            type: "numeric",
            validator: (value, callback) =>
              callback(validator.isPositive(value))
          },
          {
            data: "past_due",
            type: "numeric",
            validator: (value, callback) =>
              callback(validator.isPositive(value))
          }
        ],
        contextMenu: {
          items: {
            add_column: {
              name: "Add receipt column",
              callback: this.addColumn
            },
            remove_col: {
              callback: this.removeColumn,
              disabled: function() {
                // Disable option when first, second, third and fourth col were clicked
                // Disabled when attempt to remove all receipts cols.
                const selected = this.getSelectedLast();
                let periodsQty = this.countVisibleCols() - 4;
                let selectedQty = selected[3] - selected[1];
                selectedQty =
                  selectedQty > 0 ? selectedQty + 1 : selectedQty * -1 + 1;
                return (
                  this.getSelectedLast()[1] === 0 ||
                  this.getSelectedLast()[3] === 0 ||
                  this.getSelectedLast()[1] === 1 ||
                  this.getSelectedLast()[3] === 1 ||
                  this.getSelectedLast()[1] === 2 ||
                  this.getSelectedLast()[3] === 2 ||
                  this.getSelectedLast()[1] === 3 ||
                  this.getSelectedLast()[3] === 3 ||
                  selectedQty >= periodsQty
                );
              }
            },
            "---------": {},
            add_row: {
              name: "Add item row",
              callback: this.addRow
            },
            remove_row: {
              disabled: validator.allRowsSelected
            },
            separator: Handsontable.plugins.ContextMenu.SEPARATOR,
            copy: {},
            cut: {}
          }
        },
        rowHeights: 40,
        rowHeaders: true,
        licenseKey: "non-commercial-and-evaluation",
        className: "htMiddle htCenter",
        manualColumnResize: true,
        manualRowResize: true
      }
    };
  },
  computed: {
    ...mapGetters(["getAllInvItems", "invFile"]),
    countReceipts() {
      return this.settings.data[0].receipts.split(",").length;
    }
	},
	watch: {
		getAllInvItems() {
			this.$bvToast.show("saved-toast");
		}
	},
  created() {
    this.fetchInvFile(this.$route.params.file);
    this.fetchInvItems(this.$route.params.file);

    const unsubscribe = this.$store.subscribe(mutation => {
      if (mutation.type === "setInvItems") {
        for (let i = 1; i <= Object.keys(this.getAllInvItems[0]).length - 8; i++) {
          this.settings.colHeaders.push("Receipt " + i);
          this.settings.columns.push({
            data: "receipt" + i,
            type: "numeric",
            validator: (value, callback) =>
              callback(validator.isPositive(value))
          });
        }

				this.settings.data = this.getAllInvItems;
				unsubscribe();
      }
    });
  },
  methods: {
    ...mapActions([
      "fetchInvFile",
      "fetchInvItems",
      "updateInvItem",
      "deleteInvItem",
      "addInvItems"
    ]),
    ...mapMutations(["throwError"]),
    isValidReceipt(changes) {
      if (changes.prop.startsWith("receipt")) {
        if (!validator.isNotEmpty(changes.newValue)) {
          this.throwError("This field may not be null.");
          return false;
        } else if (!validator.isNumeric(changes.newValue)) {
          this.throwError("A valid number is required.");
          return false;
        } else if (!validator.isPositive(changes.newValue)) {
          this.throwError("Ensure this value is greater than or equal 0.");
          return false;
        }
      }

      return true;
    },
    addColumn() {
      this.settings.colHeaders.push(`Receipt  ${this.countReceipts + 1}`);
      this.settings.columns.push({
        data: `receipt${this.countReceipts + 1}`,
        type: "numeric",
        validator: (value, callback) => callback(validator.isPositive(value))
      });

      this.settings.data.forEach(item => {
        item.receipts += ",0";
        this.updateInvItem(item);
      });
    },
    removeColumn(key, selection) {
      key;
      let colStart = selection[0].start.col - 4;
      let colEnd = selection[0].end.col - 4;
      let colsQty = colEnd - colStart + 1;

      this.settings.data.forEach(elem => {
        let rec = elem.receipts.split(",");
        rec.splice(colStart, colsQty);
        elem.receipts = rec.join(",");
        this.updateInvItem(elem);
      });

      this.settings.colHeaders.splice(-colsQty, colsQty);
      this.settings.columns.splice(-colsQty, colsQty);
    },
    addRow() {
      this.addInvItems({
        items_number: 1,
        part_numbers: "-",
        receipts: "0",
        order: this.getAllInvItems.length,
        file: this.invFile.id
      });
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