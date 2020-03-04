<template>
  <div>
    <label class="title">Item Master: {{ itemMasterFile.title }}</label>
    <hot-table :settings="settings"></hot-table>
  </div>
</template>

<script>
import store from '@/store'
import { HotTable } from "@handsontable/vue";
import { mapGetters, mapActions, mapState } from "vuex";
// import Handsontable from 'handsontable';

export default {
  name: "ItemMaster",
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
        colHeaders: [
					"Part Number",
					"Class",
					"Lot Size",
					"Multiple",
					"Lead Time",
					"Yield %",
					"Unit Value",
					"Order Cost",
					"Carrying Cost",
					"Demand"
        ],
        stretchH: "all",
        colWidths: 50,
        afterChange: changes => {
          if (changes) {
            changes.forEach(([row]) => {
              this.updateItemMaster(this.settings.data[row])
            })
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
            data: "clase",
            allowEmpty: false
          },
          {
            data: "multiple",
            allowEmpty: false
          },
          {
            data: "lead_time",
            allowEmpty: false
          },
          {
            data: "yield_percent",
            allowEmpty: false
          },
          {
            data: "unit_value",
            allowEmpty: false
          },
          {
            data: "order_cost",
            allowEmpty: false
          },
          {
            data: "carrying_cost",
            allowEmpty: false
          },      
          {
            data: "demand",
            allowEmpty: false
          },
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
    ...mapGetters(["getAllItemsMasters", "getAllItemsMasters", "itemMasterFile"]),
    ...mapState({
      item_master_files: state => state.itemMasterFile
    })
  },
  
  created() {
    this.fetchitemMasterFile(this.$route.params.file);

    this.$store.subscribe(mutation => {
      if (mutation.type === "setItemsMasters") {        
        this.settings.data = this.getAllItemsMasters;
      }

      if(mutation.type === "updatedItemMaster") {
        this.$bvToast.toast("Saved successfully!", {
          title: "Storm 5.0",
          solid: true,
          variant: 'success'
        })
      }
    });
  },
  watch: {
    itemMasterFile() {
      this.fetchItemsMasters(this.$route.params.file);
    }
  },
  methods: {
    ...mapActions(["fetchitemMasterFile", "fetchItemsMasters", "updateItemMaster", "updateItemsMastersPartNumber"]),
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