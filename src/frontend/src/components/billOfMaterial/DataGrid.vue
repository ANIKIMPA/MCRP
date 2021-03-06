<template>
  <div>
    <label class="title">Bill of Material: {{ bomFile.title }}</label>
    <hot-table :settings="settings"></hot-table>
  </div>
</template>

<script>
import { HotTable } from "@handsontable/vue";
import { mapActions, mapGetters } from "vuex";
import validator from "@/js/validator";

export default {
  name: "BillOfMaterial",
  components: {
    HotTable
  },
  data() {
    return {
      settings: {
        data: [],
        colHeaders: ["Part Number", "Item Type", "PARENT", "Q/ASSY"],
        stretchH: "all",
        colWidths: 50,
        afterChange: changes => {
          if (changes) {
            changes.forEach(([row]) => {
              this.updateBomItem(this.settings.data[row]);
            });
          }
        },
        columns: [
          {
            data: "part_number",
            validator: (value, callback) =>
              callback(validator.isNotEmpty(value))
          },
          {
            data: "tipo",
            validator: (value, callback) =>
              callback(validator.isNotEmpty(value))
          },
          {
            data: "parent",
            type: "dropdown",
            source: this.allPartNumbers
          },
          {
            data: "qty",
            type: "numeric",
            validator: (value, callback) =>
              callback(validator.isPositive(value))
          }
        ],
        beforeRemoveRow: (_, amount, physicalRows) => {
          amount;
          physicalRows.forEach(index => {
            this.deleteBomItem(this.settings.data[index]);
          });
        },
        rowHeights: 40,
        rowHeaders: true,
        licenseKey: "non-commercial-and-evaluation",
        className: "htMiddle htCenter",
        manualColumnResize: true,
        manualRowResize: true,
        contextMenu: {
          items: {
            add_row: {
              name: "Add item row",
              callback: this.addRow
            },
            remove_row: {
              disabled: validator.allRowsSelected
            },
            "---------": {},
            copy: {},
            cut: {}
          }
        }
      }
    };
  },
  methods: {
    ...mapActions([
      "updateBomItem",
      "addBomItems",
      "fetchBomFile",
      "fetchBomItems",
      "deleteBomItem"
    ]),
    goBack() {
      window.history.length > 1 ? this.$router.go(-1) : this.$router.push("/");
    },
    addRow() {
      this.addBomItems({
        items_number: 1,
        file: this.$route.params.file
      });
    }
  },
  watch: {
    getAllBomItems() {
      this.settings.columns[2] = {
        data: "parent",
        type: "dropdown",
        allowEmpty: true,
        source: this.allPartNumbers
      };
      this.$bvToast.show("saved-toast");
      this.settings.data = this.getAllBomItems;
    }
  },
  computed: {
    ...mapGetters(["getAllBomItems", "bomFile"]),
    allPartNumbers() {
      return this.getAllBomItems.map(item => item.part_number);
    }
  },
  created() {
    this.fetchBomFile(this.$route.params.file);
    this.fetchBomItems(this.$route.params.file);
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

.handsontable.listbox tr td.current,
.handsontable.listbox tr:hover td {
  background: #babdbe;
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
