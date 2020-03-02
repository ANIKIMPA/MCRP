import axios from "axios";

// Computed
const state = {
  allBomFiles: [],

  bomFile: {
    title: "",
    tipo: ""
  }
};

// Computed
const getters = {
  allBomFiles: state => state.allBomFiles,
  bomFile: state => state.bomFile
};

// Methods
const actions = {
  // Obtener lista de bom files
  async fetchAllBomFiles({ commit }) {
    await axios
      .get("http://localhost:8000/api/v1.0/mrp/bom-files/")
      .then(response => {
        commit("setBomFiles", response.data);
      })
      .catch(error => {
        console.log(error);
        commit("throwError", error.response.data[Object.keys(error.response.data)[0]][0], { root: true });
      });
  },

  async fetchBomFile({ commit }, file_id) {
    await axios
      .get(`http://localhost:8000/api/v1.0/mrp/bom-files/${file_id}/`)
      .then(response => {
        commit("setBomFile", response.data);
      })
      .catch(error => {
        console.log(error);
        commit("throwError", error.response.data[Object.keys(error.response.data)[0]][0], { root: true });
      });
  },

  createNewBomFile({ commit }, file) {
    axios
      .post("http://localhost:8000/api/v1.0/mrp/bom-files/", file)
      .then(response => {
        commit("newBomFile", response.data);
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
  setBomFiles: (state, files) => (state.allBomFiles = files),
  setBomFile: (state, file) => (state.bomFile = file),
  newBomFile: (state, file) => (state.bomFile = file)
};

export default {
  state,
  getters,
  actions,
  mutations
};
