<template>
  <div id="example1">
    <hot-table :settings="settings"> </hot-table>

    <b-toast id="my-toast" variant="success" solid>
      <template v-slot:toast-title>
        <div class="d-flex flex-grow-1 align-items-baseline">
          <strong class="mr-auto">Storm 5.0</strong>
        </div>
      </template>
      Saved successfully!
    </b-toast>
  </div>
</template>

<script>
import { HotTable } from "@handsontable/vue";
import { mapActions } from "vuex";

export default {
  components: {
    HotTable
    // HotColumn
  },
  data() {
    return {
      items: [],
      settings: {
        data: [],
        colHeaders: ["Part Number", "Item Type", "PARENT", "Q/ASSY"],
        stretchH: "all",
        colWidths: 300,
        afterChange: changes => {
          if (changes) {
            changes.forEach(([row]) => {
              try {
                this.updateItem(this.settings.data[row]);
                this.$bvToast.show('my-toast')
              }
              catch(error) {
                console(error)
              }
            });
          }
        },
        beforeRender: () => {
          this.storeItems(this.settings.data);
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
            data: "parent"
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
        contextMenu: [
          "row_above",
          "row_below",
          "---------",
          "remove_row",
          "---------",
          "undo",
          "redo",
          "---------",
          "make_read_only",
          "---------",
          "alignment",
          "---------",
          "copy",
          "cut"
        ]
      }
    };
  },
  methods: {
    ...mapActions(["storeItems", "updateItem"]),
    check() {
      console.log();
    }
  }
};
</script>

<style>
@import "~handsontable/dist/handsontable.full.css";
</style>
