import axios from "axios";

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
    await axios
      .get("http://localhost:8000/api/v1.0/mrp/inv-files/")
      .then(response => {
        commit("setInvFiles", response.data);
      })
      .catch(error => {
        console.log(error)
        commit("throwError", error.response.data[Object.keys(error.response.data)[0]][0], { root: true });
      });
  },

  async fetchInvFile({ commit }, file_id) {
    await axios
      .get(`http://localhost:8000/api/v1.0/mrp/inv-files/${file_id}/`)
      .then(response => {
        commit("setInvFile", response.data);
      })
      .catch(error => {
        console.log(error)
        commit("throwError", error.response.data[Object.keys(error.response.data)[0]][0], { root: true });
      });
  },

  createNewInvFile({ commit }, file) {
    axios
      .post("http://localhost:8000/api/v1.0/mrp/inv-files/", file)
      .then(response => {
        commit("newInvFile", response.data);
      })
      .catch(error => {
        console.log(error)
        commit("throwError", error.response.data[Object.keys(error.response.data)[0]][0], { root: true });
      });
  }
};

// Methods
const mutations = {
  // Set all files to state
  setInvFiles: (state, files) => (state.allInvFiles = files),
  setInvFile: (state, file) => (state.invFile = file),
  newInvFile: (state, file) => (state.invFile = file)
};

export default {
  state,
  getters,
  actions,
  mutations
};