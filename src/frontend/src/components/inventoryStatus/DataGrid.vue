<template>
  <div>
    <label class="title">{{ invFile.title }}</label>
    <hot-table :settings="settings"></hot-table>

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
import store from '@/store'
import { HotTable } from "@handsontable/vue";
import { mapGetters, mapActions, mapState } from "vuex";
// import Handsontable from 'handsontable';

export default {
  name: "inventory_status",
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
        colHeaders: ["Part Number"],
        stretchH: "all",
        colWidths: 50,
        afterChange: changes => {
          if (changes) {
            changes.forEach(([row, prop, oldValue, newValue]) => {
              oldValue;
                this.updatePeriod({ row, prop, newValue });
            });
          }
        },
        columns: [],
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
    ...mapGetters(["getAllPeriods", "getAllConvertedPeriods", "invFile"]),
    ...mapState({
      inv_files: state => state.invFile
    })
  },
  
  created() {
    this.fetchMastFile(this.$route.params.file);

    this.$store.subscribe(mutation => {
      if (mutation.type === "setPeriods") {
        this.settings.columns.push({
          data: "part_number",
          allowEmpty: false
        });
        for (let i = 0; i < this.invFile.planning_horizon_length * 1; i++) {
          this.settings.colHeaders.push("Period " + (i + 1));
          this.settings.columns.push({
            data: this.getAllPeriods[i].order,
            type: "numeric",
            allowEmpty: true
          });
        }
        
        this.settings.data = this.getAllConvertedPeriods;
      }

      if(mutation.type === "updatedPeriod") {
        this.$bvToast.show("my-toast");
      }
    });
  },
  watch: {
    invFile() {
      this.fetchPeriods(this.$route.params.file);
    }
  },
  methods: {
    ...mapActions(["fetchMastFile", "fetchPeriods", "updatePeriod", "updatePeriodsPartNumber"])
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