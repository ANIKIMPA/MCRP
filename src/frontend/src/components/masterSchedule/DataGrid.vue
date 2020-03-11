<template>
  <div>
    <label class="title">Master Schedule: {{ mastFile.title }}</label>
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
  name: "MasterSchedule",
  store,
  components: {
    HotTable
  },
  data() {
    return {
      settings: {
        data: [],
        colHeaders: ["Part Number"],
        stretchH: "all",
        colWidths: 50,
        afterChange: changes => {
          if (changes) {
            changes.forEach(([row, prop, oldValue, newValue]) => {
              if (this.isValidPeriod({ row, prop, oldValue, newValue })) {
                // Obteniendo todos los keys que empiecen con period
                let keys = Object.keys(this.settings.data[row]).filter(
                  key => key.startsWith("period") && key != "periods"
                );
                // Guardando todos los periods en la propiedad periods
                this.settings.data[row].periods = keys
                  .map(key => this.settings.data[row][key])
                  .join(",");

                this.updateMastItem(this.settings.data[row]);
              }
            });
          }
        },
        beforeRemoveRow: (_, amount, physicalRows) => {
          amount;

          physicalRows.forEach(index => {
            this.deleteMastItem(this.settings.data[index]);
          });
        },
        columns: [
          {
            data: "part_number",
            validator: (value, callback) =>
              callback(validator.isNotEmpty(value))
          }
        ],
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
    ...mapGetters(["getAllMastItems", "mastFile"]),
    countPeriods() {
      return this.settings.data[0].periods.split(",").length;
    }
  },
  created() {
    this.fetchMastFile(this.$route.params.file);
    this.fetchMastItems(this.$route.params.file);

    this.settings.contextMenu = {
      items: {
        add_row: {
          name: "Add item row",
          callback: this.addRow
        },
        remove_row: {
          disabled: validator.allRowsSelected
        },
        "---------": {},
        add_column: {
          name: "Add period column",
          callback: this.addColumn
        },
        remove_col: {
          callback: this.removeColumn,
          disabled: function() {
            // Disable option when first col was selected or when attempt to remove all periods
            const selected = this.getSelectedLast();
            let periodsQty = this.countVisibleCols() - 1;
            let selectedQty = selected[3] - selected[1];
            selectedQty =
              selectedQty > 0 ? selectedQty + 1 : selectedQty * -1 + 1;
            return (
              selected[1] === 0 ||
              selected[3] === 0 ||
              selectedQty >= periodsQty
            );
          }
        },
        separator: Handsontable.plugins.ContextMenu.SEPARATOR,
        copy: {},
        cut: {}
      }
    };

    this.$store.subscribe(mutation => {
      if (mutation.type === "setMastItems") {
        for (let i = 1; i <= Object.keys(this.getAllMastItems[0]).length - 5; i++) {
          this.settings.colHeaders.push("Period " + i);
          this.settings.columns.push({
            data: "period" + i,
            type: "numeric",
            validator: (value, callback) =>
              validator.isPositive(value) ? callback(true) : callback(false)
          });
        }

        this.settings.data = this.getAllMastItems;
      }

      if (
        mutation.type === "updatedMastItem" ||
        mutation.type === "deletedMastItem"
      ) {
        this.$bvToast.show("saved-toast");
      }
    });
  },
  methods: {
    ...mapActions([
      "fetchMastFile",
      "fetchMastItems",
      "updateMastItem",
      "deleteMastItem",
      "addMastItems"
    ]),
    ...mapMutations(["throwError"]),
    isValidPeriod(changes) {
      if (changes.prop.startsWith("period")) {
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
      this.settings.colHeaders.push(`Period  ${this.countPeriods + 1}`);
      this.settings.columns.push({
        data: `period${this.countPeriods + 1}`,
        type: "numeric",
        validator: validator.isPositive
      });

      this.settings.data.forEach(item => {
        item.periods += ",0";
        this.updateMastItem(item);
      });
    },
    removeColumn(key, selection) {
      key;
      let colStart = selection[0].start.col - 1;
      let colEnd = selection[0].end.col - 1;
      let colsQty = colEnd - colStart + 1;

      this.settings.data.forEach(elem => {
        let rec = elem.periods.split(",");
        rec.splice(colStart, colsQty);
        elem.periods = rec.join(",");
        this.updateMastItem(elem);
      });

      this.settings.colHeaders.splice(-colsQty, colsQty);
      this.settings.columns.splice(-colsQty, colsQty);
    },
    addRow() {
      let periods = [];
      this.settings.colHeaders.forEach(header => {
        if (header.startsWith("Period")) periods.push("0");
      });

      this.addMastItems({
        items_number: 1,
        part_numbers: "-",
        createFromBomFile: false,
        periods: periods.join(","),
        order: this.getAllMastItems.length,
        file: this.mastFile.id,
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