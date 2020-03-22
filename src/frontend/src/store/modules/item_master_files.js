import { AxiosBase } from "@/api/axios-base";
import functions from "@/js/functions";

// Computed
const state = {
  allItemMasterFiles: [],

  itemMasterFile: {
    title: "",
    tipo: ""
  }
};

// Computed
const getters = {
  allItemMasterFiles: state => state.allItemMasterFiles,
  itemMasterFile: state => state.itemMasterFile
};

// Methods
const actions = {
  // Obtener lista de item master files
  async fetchAllItemMasterFiles({ commit }) {
    await AxiosBase
      .get("mrp/item-master-files/")
      .then(response => {
        commit("setItemMasterFiles", response.data);
      })
      .catch(error => {
        for (let value of Object.values(error.response.data)) {
          commit("throwError", value, { root: true });
        }
      });
  },

  async fetchItemMasterFile({ commit }, file_id) {
    await AxiosBase
      .get(`mrp/item-master-files/${file_id}/`)
      .then(response => {
        commit("setItemMasterFile", response.data);
      })
      .catch(error => {
        for (let value of Object.values(error.response.data)) {
          commit("throwError", value, { root: true });
        }
      });
  },

  createNewItemMasterFile({ commit }, file) {
    AxiosBase
      .post("mrp/item-master-files/", file)
      .then(response => {
        commit("newItemMasterFile", response.data);
      })
      .catch(error => {
        for (let value of Object.values(error.response.data)) {
          commit("throwError", value, { root: true });
        }
      });
  },

  async deleteItemMasterFile({ commit }, file) {
    await AxiosBase
      .put(`mrp/item-master-files/${file.id}/`, file)
      .then(() => {
        commit("deletedItemMasterFile", file);
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
  setItemMasterFiles: (state, files) => (state.allItemMasterFiles = files),
  setItemMasterFile: (state, file) => (state.itemMasterFile = file),
  newItemMasterFile: (state, file) => (state.itemMasterFile = file),
  deletedItemMasterFile: (state, file) =>  functions.remove(state.allItemMasterFiles, file)
};

export default {
  state,
  getters,
  actions,
  mutations
};