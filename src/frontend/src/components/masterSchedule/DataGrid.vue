<template>
  <div>
    <label class="title">Master Schedule: {{ mastFile.title }}</label>
    <hot-table :settings="settings"></hot-table>
  </div>
</template>

<script>
import store from "@/store";
import { HotTable } from "@handsontable/vue";
import { mapGetters, mapActions } from "vuex";
import Handsontable from "handsontable";
import validator from '@/js/validator';

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
            changes.forEach(([row]) => {
              // Obteniendo todos los keys que empiecen con period
              let keys = Object.keys(this.settings.data[row]).filter(
                key => key.startsWith("period") && key != "periods"
              );
              // Guardando todos los periods en la propiedad periods
              this.settings.data[row].periods = keys.map(key => this.settings.data[row][key]).join(",");

              this.updateMastItem(this.settings.data[row])
            });
          }
        },
        beforeRemoveRow: (_, amount, physicalRows) => {
          console.log(amount)

          physicalRows.forEach(index => {
            this.deleteMastItem(this.settings.data[index]);
          })
        },
        columns: [
          {
            data: "part_number",
            validator: validator.isNotEmpty
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
    ...mapGetters(["getAllMastItems", "getAllMastItems", "mastFile"]),
    countPeriods() {
      return this.settings.data[0].periods.split(",").length;
    }
  },

  created() {
    this.fetchMastFile(this.$route.params.file);
    this.fetchMastItems(this.$route.params.file);

    this.$store.subscribe(mutation => {
      if (mutation.type === "setMastItems") {
        for (let i = 1; i <= Object.keys(this.getAllMastItems[0]).length - 4; i++) {
          this.settings.colHeaders.push("Period " + i);
          this.settings.columns.push({
            data: "period" + i,
            type: 'numeric',
            validator: validator.isPositive
          });
        }

        this.settings.data = this.getAllMastItems;
      }

      this.settings.contextMenu = {
        items: {
          add_column: {
            name: "Add period column",
            callback: this.addColumn
          },
          remove_col: {
            callback: this.removeColumn,
            disabled: function() {
              // Disable option when first col was clicked
              return (
                this.getSelectedLast()[1] === 0
              );
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

      if (mutation.type === "updatedMastItem") {
        this.$bvToast.show("saved-toast");
      } else if(mutation.typ === "deletedMastItem") {
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
      "addMastItem"
    ]),
    addColumn() {
      this.settings.colHeaders.push(`Period  ${this.countPeriods + 1}`);
      this.settings.columns.push({
        data: `period${this.countPeriods + 1}`,
        type: 'numeric',
        validator: validator.isPositive
      });

      this.settings.data.forEach(item => {
        item.periods += ",0";
        this.updateMastItem(item);
      });
    },
    removeColumn(key, selection) {
      key
      let colStart = selection[0].start.col - 4;
      let colEnd = selection[0].end.col - 4;
      let colsQty = colEnd - colStart + 1

      this.settings.data.forEach(elem => {
        let rec = elem.periods.split(",")
        rec.splice(colStart, colsQty)
        elem.periods = rec.join(",")
        this.updateMastItem(elem)
      })

      this.settings.colHeaders.splice(-colsQty, colsQty);
      this.settings.columns.splice(-colsQty, colsQty);
    },
    addRow() {
      const item = {
        part_number: "-",
        safe_stock: 0,
        on_hand: 0,
        past_due: 0,
        periods: "0",
        file: this.mastFile.id
      }

      this.addMastItem(item);
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