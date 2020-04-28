import { AxiosBase } from "@/api/axios-base";
import functions from "@/js/functions";

// Computed
const state = {
  allReports: [],

  report: {
    title: "",
    items: []
  }
};

// Computed
const getters = {
    allReports: state => state.allReports,
    report: state => state.report
};

// Methods
const actions = {
  // Obtener lista de inv reports
  async fetchAllReports({ commit }) {
    return new Promise((resolve, reject) => {
      AxiosBase
        .get("mrp/reports/")
        .then(response => {
          commit("setAllReports", response.data);
          resolve()
        })
        .catch(() => {
          reject()
        })
    })
  },

  async fetchReport({ commit }, report_id) {
    return await AxiosBase
      .get(`mrp/reports/${report_id}/`)
      .then(response => {
        commit("setReport", response.data);
      })      
  },

  async createNewReport({ commit }, report) {
    return await AxiosBase
        .post("mrp/reports/", report)
        .then(response => {
            commit("setReport", response.data);
        })
  },

  async updateReport({ commit }, report) {
    return await AxiosBase
        .put(`mrp/reports/${report.id}/`, report)
        .then(response => {
            commit("setReport", response.data);
        })
  },

  async deleteReport({ commit }, report) {
    return await AxiosBase
      .put(`mrp/reports/${report.id}/`, report)
      .then(() => {
        commit("deletedReport", report);
      })
  }
};

// Methods
const mutations = {
  // Set all reports to state
  setAllReports: (state, reports) => (state.allReports = reports),
  setReport: (state, report) => (state.report = report),
  setReportItems: (state, items) => (state.report.items = items),
  setReportTitle: (state, title) => (state.report.title = title),
  deletedReport: (state, report) =>  functions.remove(state.allReports, report)
};

export default {
  state,
  getters,
  actions,
  mutations
};