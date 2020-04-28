<template>
  <div>
    <li @click="openModal">Reports</li>
    <b-modal id="report-list" v-model="modalOpenned" title="Report Files" hide-footer>
      <p class="mb-2">Select Report:</p>

      <b-list-group class="overflow-auto mh-300">
        <b-list-group-item v-if="loading" class="text-center">
          <b-spinner label="Spinning"></b-spinner>
        </b-list-group-item>
        <b-list-group-item
          button
          v-for="report in allReports"
          @click="openReport(report)"
          :key="report.id"
          class="d-flex justify-content-between"
        >
          <span style="width: 50%">
            <i class="fas fa-file-alt"></i>
            {{ report.title }}
          </span>
          <small style="font-style: italic;">{{ report.created_date | formatDate }}</small>
          <a
            href="#"
            @click.stop.prevent="deleteFile(report)"
            class="text-danger px-1"
            style="text-align:right;"
          >
            <i class="fas fa-trash-alt"></i>
          </a>
        </b-list-group-item>
      </b-list-group>
    </b-modal>
  </div>
</template>

<script>
import moment from "moment";
import { mapActions, mapGetters } from "vuex";
export default {
  name: "SelectReport",
  data() {
    return {
      modalOpenned: false,
      loading: true
    };
  },
  filters: {
    formatDate(value) {
      return moment(value).format("L") + " " + moment(value).format("hh:mma");
    }
  },
  methods: {
    ...mapActions(["fetchAllReports", "deleteReport"]),
    openReport(report) {
      this.$router.push({
        name: "final_report",
        params: {
          report: report.id
        }
      });
      this.$bvModal.hide("report-list");
    },
    openModal() {
      this.modalOpenned = true;
      this.fetchAllReports()
      .then(() => {
        this.loading = false;
      });
    },
    deleteFile(report) {
        if (this.report.id === report.id) {
            this.$router.push("/");
        }
        report.removed = true;
        this.deleteReport(report);
    }
  },
  computed: {
    ...mapGetters(["allReports", "report"])
  }
};
</script>

<style>
.mh-300 {
  max-height: 300px;
}
</style>