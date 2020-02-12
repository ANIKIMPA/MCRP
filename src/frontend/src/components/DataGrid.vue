<template>
  <div id="example1">
    <hot-table ref="wrapper" :settings="settings"> </hot-table>

    <b-toast id="my-toast" variant="success" solid>
      <template v-slot:toast-title>
        <div class="d-flex flex-grow-1 align-items-baseline">
          <strong class="mr-auto">Storm 5.0</strong>
        </div>
      </template>
      Saved successfully!
    </b-toast>

    <button @click="check">Check</button>
  </div>
</template>

<script>
import { HotTable } from "@handsontable/vue";
import { mapActions } from "vuex";

export default {
  name: "file",
  components: {
    HotTable
    // HotColumn
  },
  data() {
    return {
      fileId: this.$route.params.file,
      hotRef: null,
      funcion: function(context) {
        context.addItem({
          part_number: null,
          tipo: "MAT",
          parent: null,
          qty: 1,
          file: this.fileId,
        })
      },
      settings: {
        data: [],
        colHeaders: ["Part Number", "Item Type", "PARENT", "Q/ASSY"],
        stretchH: "all",
        colWidths: 300,
        afterChange: changes => {
          if (changes) {
            changes.forEach(([row]) => {
              try {
                console.log(this.settings.data[row]);
                this.updateItem(this.settings.data[row]);
                this.$bvToast.show("my-toast");
              } catch (error) {
                console(error);
              }
            });
          }
        },
        beforeRender: () => {
          // this.storeItems(this.settings.data);
        },
        afterRender: () => {
          this.settings.contextMenu.items.insert_row = {}
          this.settings.contextMenu.items.insert_row.name = "Insert new row"
          this.settings.contextMenu.items.insert_row.callback = this.funcion(this)
        },
        beforeOnCellMouseDown: () => {
          console.log("aqui")
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
        caritas: "Carita",
        contextMenu: {
          items: {
            remove_row: {},
            "---------": {},
            undo: {},
            redo: {},
            copy: {},
            cut: {},
          }
        }
      }
    };
  },
  methods: {
    ...mapActions(["storeItems", "updateItem", "addItem"]),
    check() {
    }
  },
  mounted: function() {
    this.hotRef = this.$refs.wrapper.hotInstance;
    this.$store.commit('updateItems', this.hotRef.getSourceData());
  },
};
</script>

<style>
@import "~handsontable/dist/handsontable.full.css";
</style>
