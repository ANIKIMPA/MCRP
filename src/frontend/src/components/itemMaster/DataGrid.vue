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
            data: "lot_size",
            type: 'dropdown',
            source: ['LFL', 'FP', 'FQ', 'EOQ']
          },
          {
            data: "multiple",
            type: 'numeric',
            validator: this.isPositive,
          },
          {
            data: "lead_time",
            type: 'numeric',
            validator: this.isPositive,
          },
          {
            data: "yield_percent",
            validator: this.isValidPercent,
            type: 'numeric',
            numericFormat: {
              pattern: '0%',
              culture: 'en-US'
            }
          },
          {
            data: "unit_value",
            type: 'numeric',
            validator: this.isPositive,
          },
          {
            data: "order_cost",
            validator: this.isPositive,
            type: 'numeric',
            numericFormat: {
              pattern: '$0,0.00',
              culture: 'en-US'
            }
          },
          {
            data: "carrying_cost",
            validator: this.isPositive,
            type: 'numeric',
            numericFormat: {
              pattern: '$0,0.00',
              culture: 'en-US'
            }
          },      
          {
            data: "demand",
            type: 'numeric',
            validator: this.isPositive,
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
    this.fetchItemMasterFile(this.$route.params.file);

    this.$store.subscribe(mutation => {
      if (mutation.type === "setItemsMasters") {        
        this.settings.data = this.getAllItemsMasters;
      }

      if(mutation.type === "updatedItemMaster")
        this.$bvToast.show("saved-toast");
    });
  },
  watch: {
    itemMasterFile() {
      this.fetchItemsMasters(this.$route.params.file);
    }
  },
  methods: {
    ...mapActions(["fetchItemMasterFile", "fetchItemsMasters", "updateItemMaster"]),
    isPositive(value, callback) {
      if(typeof(value) === "number") {
        callback(value >= 0)
      }
      else {
        callback(false)
      }
    },
    isValidPercent(value, callback) {
      if(typeof(value) === "number") {
        callback(value >= 0 && value <= 1)
      }
      else {
        callback(false)
      }
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