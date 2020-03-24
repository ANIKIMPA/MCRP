import { AxiosBase } from "@/api/axios-base";
import functions from "@/js/functions";

// Computed
const state = {
  allMastFiles: [],

  mastFile: {
    title: "",
    tipo: ""
  }
};

// Computed
const getters = {
  allMastFiles: state => state.allMastFiles,
  mastFile: state => state.mastFile
};

// Methods
const actions = {
  // Obtener lista de files
  async fetchAllMastFiles({ commit }) {
    return new Promise((resolve, reject) => {
      AxiosBase.get("mrp/mast-files/")
        .then(response => {
          commit("setMastFiles", response.data);
          resolve();
        })
        .catch(() => {
          reject();
        });
    });
  },

  async fetchMastFile({ commit }, file_id) {
    await AxiosBase.get(`mrp/mast-files/${file_id}/`)
      .then(response => {
        commit("setMastFile", response.data);
      })      
  },

  createNewMastFile({ commit }, file) {
    AxiosBase.post("mrp/mast-files/", file)
      .then(response => {
        commit("newMastFile", response.data);
      })      
  },

  async deleteMastFile({ commit }, file) {
    await AxiosBase.put(`mrp/mast-files/${file.id}/`, file)
      .then(() => {
        commit("deletedMastFile", file);
      })      
  }
};

// Methods
const mutations = {
  // Set all files to state
  setMastFiles: (state, files) => (state.allMastFiles = files),
  setMastFile: (state, file) => (state.mastFile = file),
  newMastFile: (state, file) => (state.mastFile = file),
  deletedMastFile: (state, file) => functions.remove(state.allMastFiles, file)
};

export default {
  state,
  getters,
  actions,
  mutations
};
