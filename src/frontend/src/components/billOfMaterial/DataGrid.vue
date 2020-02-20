<template>
  <div id="example1">
    <hot-table :settings="settings"></hot-table>

    <b-toast id="my-toast" variant="success" solid>
      <template v-slot:toast-title>
        <div class="d-flex flex-grow-1 align-items-baseline">
          <strong class="mr-auto">Storm 5.0</strong>
        </div>
      </template>
      Saved successfully!
    </b-toast>

    <b-button  class="position-absolute btnAddItem" variant="info" @click="addRow">Add new item</b-button>
  </div>
</template>

<script>
import { HotTable } from "@handsontable/vue";
import { mapActions, mapGetters } from "vuex";

export default {
  name: "billOfMaterial",
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
            changes.forEach(([row]) => {
              try {
                this.updateItem(this.settings.data[row]);
                this.$bvToast.show("my-toast");
              } catch (error) {
                console(error);
              }
            });
          }
        },
        columns: [
          {
            data: "part_number",
            allowEmpty: false
          },
          {
            data: "tipo",
            allowEmpty: false
          },
          {
            data: "qty",
            type: "numeric",
            allowEmpty: false
          }
        ],
        rowHeights: 40,
        rowHeaders: true,
        licenseKey: "non-commercial-and-evaluation",
        className: "htMiddle htCenter",
        contextMenu: {
          items: {
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
    ...mapActions(["updateItem", "addItem", "fetchBomFile", "fetchItems"]),
    addRow() {
      this.addItem({
        part_number: null,
        tipo: "MAT",
        parent: null,
        qty: 1,
        file: this.$route.params.file
      });
      this.$bvToast.show("my-toast");
    }
  },
  computed: {
    ...mapGetters(["getAllItems"]),
    allPartNumbers() {
      let part_numbers = [];

      for (let i = 0; i < this.getAllItems.length; i++) {
        part_numbers.push(this.getAllItems[i].part_number);
      }

      return part_numbers;
    }
  },
  mounted: function() {
    this.fetchBomFile(this.$route.params.file);
    this.fetchItems(this.$route.params.file);

    this.$store.subscribe(mutation => {
      if (mutation.type === "setItems") {
        this.settings.columns.push({
          data: "parent",
          type: 'dropdown',
          source: this.allPartNumbers
          // editor: "select",
          // selectOptions: this.allPartNumbers
        });
        this.settings.data = this.getAllItems;
      }
    });
  }
};
</script>

<style>
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

.btnAddItem {
  top: 65px;
  left: 50%;
}
</style>
