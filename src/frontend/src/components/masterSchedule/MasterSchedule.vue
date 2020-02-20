<template>
  <div>
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
  name: "master_schedule",
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
        colWidths: 100,
        afterChange: changes => {
          if (changes) {
            changes.forEach(([row, prop, oldValue, newValue]) => {
              row;
              oldValue;
              try {
                let period = this.getAllPeriods.find(
                  period => period.id == prop
                );
                period.data = newValue;
                this.updatePeriod(period);
                this.$bvToast.show("my-toast");
              } catch (error) {
                console.log(error);
              }
            });
          }
        },
        columns: [],
        rowHeights: 40,
        rowHeaders: true,
        licenseKey: "non-commercial-and-evaluation",
        className: "htMiddle htCenter"
      }
    };
  },
  computed: {
    ...mapGetters(["getAllPeriods", "getAllConvertedPeriods", "mastFile"]),
    ...mapState({
      mast_files: state => state.mastFile
    })
  },
  
  mounted() {
    this.fetchMastFile(this.$route.params.file);

    this.$store.subscribe(mutation => {
      if (mutation.type === "setPeriods") {
        this.settings.columns.push({
          data: "part_number",
          allowEmpty: false,
          readOnly: true
        });
        for (let i = 0; i < this.mastFile.planning_horizon_length * 1; i++) {
          this.settings.colHeaders.push("Period " + (i + 1));
          this.settings.columns.push({
            data: this.getAllPeriods[i].id,
            allowEmpty: true
          });
        }
        
        this.settings.data = this.getAllConvertedPeriods;
      }
    });
  },
  watch: {
    mastFile() {
      this.fetchPeriods(this.$route.params.file);
    }
  },
  methods: {
    ...mapActions(["fetchMastFile", "fetchPeriods", "updatePeriod"])
  }
};
</script>

<style>
@import "~handsontable/dist/handsontable.full.css";
</style>