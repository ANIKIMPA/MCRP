import axios from "axios";

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
    await axios
      .get("http://localhost:8000/api/v1.0/mrp/item-master-files/")
      .then(response => {
        commit("setItemMasterFiles", response.data);
      })
      .catch(error => {
        console.log(error);
        commit("throwError", error.response.data[Object.keys(error.response.data)[0]][0], { root: true });
      });
  },

  async fetchItemMasterFile({ commit }, file_id) {
    await axios
      .get(`http://localhost:8000/api/v1.0/mrp/item-master-files/${file_id}/`)
      .then(response => {
        commit("setItemMasterFile", response.data);
      })
      .catch(error => {
        console.log(error);
        commit("throwError", error.response.data[Object.keys(error.response.data)[0]][0], { root: true });
      });
  },

  createNewItemMasterFile({ commit }, file) {
    axios
      .post("http://localhost:8000/api/v1.0/mrp/item-master-files/", file)
      .then(response => {
        commit("newItemMasterFile", response.data);
      })
      .catch(error => {
        console.log(error);
        commit("throwError", error.response.data[Object.keys(error.response.data)[0]][0], { root: true });
      });
  }
};

// Methods
const mutations = {
  // Set all files to state
  setItemMasterFiles: (state, files) => (state.allItemMasterFiles = files),
  setItemMasterFile: (state, file) => (state.itemMasterFile = file),
  newItemMasterFile: (state, file) => (state.itemMasterFile = file)
};

export default {
  state,
  getters,
  actions,
  mutations
};