import { AxiosBase } from "@/api/axios-base";
import functions from "@/js/functions";

// Computed
const state = {
  allInvFiles: [],

  invFile: {
    title: "",
    tipo: ""
  }
};

// Computed
const getters = {
  allInvFiles: state => state.allInvFiles,
  invFile: state => state.invFile
};

// Methods
const actions = {
  // Obtener lista de inv files
  async fetchAllInvFiles({ commit }) {
    await AxiosBase
      .get("mrp/inv-files/")
      .then(response => {
        commit("setInvFiles", response.data);
      })
      .catch(error => {
        for (let value of Object.values(error.response.data)) {
          commit("throwError", value, { root: true });
        }
      });
  },

  async fetchInvFile({ commit }, file_id) {
    await AxiosBase
      .get(`mrp/inv-files/${file_id}/`)
      .then(response => {
        commit("setInvFile", response.data);
      })
      .catch(error => {
        for (let value of Object.values(error.response.data)) {
          commit("throwError", value, { root: true });
        }
      });
  },

  createNewInvFile({ commit }, file) {
    AxiosBase
      .post("mrp/inv-files/", file)
      .then(response => {
        commit("newInvFile", response.data);
      })
      .catch(error => {
        for (let value of Object.values(error.response.data)) {
          commit("throwError", value, { root: true });
        }
      });
  },

  async deleteInvFile({ commit }, file) {
    await AxiosBase
      .put(`mrp/inv-files/${file.id}/`, file)
      .then(() => {
        commit("deletedInvFile", file);
      })
      .catch(error => {
        for (let value of Object.values(error.response.data)) {
          commit("throwError", value, { root: true });
        }
      });
  }
};

// Methods
const mutations = {
  // Set all files to state
  setInvFiles: (state, files) => (state.allInvFiles = files),
  setInvFile: (state, file) => (state.invFile = file),
  newInvFile: (state, file) => (state.invFile = file),
  deletedInvFile: (state, file) =>  functions.remove(state.allInvFiles, file)
};

export default {
  state,
  getters,
  actions,
  mutations
};