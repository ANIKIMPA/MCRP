<template>
  <div>
    <hot-table ref="hotTableComponent" :settings="settings"></hot-table>

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
import { mapGetters } from "vuex";
// import Handsontable from 'handsontable';

export default {
  name: "master_schedule",
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
        colWidths: 300,
        afterChange: changes => {
          if (changes) {
            changes.forEach(([row]) => {
              try {
                this.updateMasterSchedule(this.settings.data[row]);
                this.$bvToast.show("my-toast");
              } catch (error) {
                console(error);
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
    ...mapGetters(["getAllMastersSchedules"])
  },
  created() {
    console.log(this.$route.params.numberOfPeriods);
    this.settings.columns.push({
      data: "part_number",
      allowEmpty: false
    });
    for (let i = 1; i <= this.$route.params.numberOfPeriods * 1; i++) {
      this.settings.colHeaders.push("Period " + i);
      this.settings.columns.push({
        data: "period" + i,
        allowEmpty: false
      });
    }
  },
  mounted: function() {
    this.hotRef = this.$refs.hotTableComponent.hotInstance;
    this.$store.commit("updateMastersSchedules", this.hotRef.getSourceData());
  }
};
</script>

<style>
@import "~handsontable/dist/handsontable.full.css";
</style>