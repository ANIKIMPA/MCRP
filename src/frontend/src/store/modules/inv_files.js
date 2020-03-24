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
    return new Promise((resolve, reject) => {
      AxiosBase
        .get("mrp/inv-files/")
        .then(response => {
          commit("setInvFiles", response.data);
          resolve()
        })
        .catch(() => {
          reject()
        })
    })
  },

  async fetchInvFile({ commit }, file_id) {
    await AxiosBase
      .get(`mrp/inv-files/${file_id}/`)
      .then(response => {
        commit("setInvFile", response.data);
      })      
  },

  createNewInvFile({ commit }, file) {
    AxiosBase
      .post("mrp/inv-files/", file)
      .then(response => {
        commit("newInvFile", response.data);
      })      
  },

  async deleteInvFile({ commit }, file) {
    await AxiosBase
      .put(`mrp/inv-files/${file.id}/`, file)
      .then(() => {
        commit("deletedInvFile", file);
      })      
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