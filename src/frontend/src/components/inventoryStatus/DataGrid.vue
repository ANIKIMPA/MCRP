<template>
  <div>
    <label class="title">Inventory Status: {{ invFile.title }}</label>
    <hot-table :settings="settings"></hot-table>

    <b-button  class="position-absolute btnAddReceipt" variant="info" @click="addReceipt">Add Receipt</b-button>
  </div>
</template>

<script>
import store from '@/store'
import { HotTable } from "@handsontable/vue";
import { mapGetters, mapActions, mapState } from "vuex";
// import Handsontable from 'handsontable';

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
              oldValue;
              if(!newValue || newValue.trim() == "") {
                this.$bvToast.toast("Cell cannot be empty.", {
                  title: "Storm 5.0",
                  solid: true,
                  variant: 'danger'
                })
              } else if(isNaN(newValue) && prop !== "part_number") {
                this.$bvToast.toast("A valid integer is required.", {
                  title: "Storm 5.0",
                  solid: true,
                  variant: 'danger'
                })
              }
              else {
                // Obteniendo todos los keys que empiecen con receipt      
                let keys = Object.keys(this.settings.data[row]).filter(key => key.startsWith('receipt') && key != "receipts")
                // Guardando todos los receipts en la propiedad receipts
                this.settings.data[row].receipts = keys.map(key => this.settings.data[row][key]).join(',')
  
                this.updateInvItem(this.settings.data[row])
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
            data: "safe_stock",
            allowEmpty: false
          },
          {
            data: "on_hand",
            allowEmpty: false
          },
          {
            data: "past_due",
            allowEmpty: false
          }          
        ],
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
        for(let i = 1; i <= Object.keys(this.getAllInvItems[0]).length - 7; i++) {
          this.settings.colHeaders.push("Receipt " + i);
          this.settings.columns.push({
            data: "receipt" + i,
            type: "numeric",
            allowEmpty: false
          });
        }
        
        this.settings.data = this.getAllInvItems;
      }

      if(mutation.type === "updatedInvItem") {
        this.$bvToast.toast("Saved successfully!", {
          title: "Storm 5.0",
          solid: true,
          variant: 'success'
        })
      }
    });
  },
  watch: {
    invFile() {
      this.fetchInvItems(this.$route.params.file);
    }
  },
  methods: {
    ...mapActions(["fetchInvFile", "fetchInvItems", "updateInvItem", "updateInvItemsPartNumber"]),
    addReceipt() {
      this.settings.colHeaders.push(`Receipt  ${this.countReceipts + 1}`);
      this.settings.columns.push({
        data: `receipt${this.countReceipts + 1}`,
        type: "numeric",
        allowEmpty: false
      });

      this.settings.data.forEach(item => {
        item.receipts += ",0";
        this.updateInvItem(item)
      })
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

.btnAddReceipt {
  top: 62px;
  left: 30%;
}
</style>