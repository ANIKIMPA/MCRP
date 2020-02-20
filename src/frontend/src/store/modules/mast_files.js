import axios from "axios";

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
    await axios
      .get("http://localhost:8000/api/v1.0/mrp/mast-files/")
      .then(response => {
        commit("setMastFiles", response.data);
      })
      .catch(error => {
        console.log(error);
      });
  },
  
  async fetchMastFile({ commit }, file_id) {
    await axios
      .get(`http://localhost:8000/api/v1.0/mrp/mast-files/${file_id}/`)
      .then(response => {
        commit("setMastFile", response.data);
      })
      .catch(error => {
        console.log(error);
      });
	},
	
  createNewMastFile({ commit }, file) {
    axios
      .post("http://localhost:8000/api/v1.0/mrp/mast-files/", file)
      .then(response => {
        commit("newMastFile", response.data);
      })
      .catch(error => {
        console.log(error);
      });
  }
};

// Methods
const mutations = {
  // Set all files to state
  setMastFiles: (state, files) => (state.allMastFiles = files),
  setMastFile: (state, file) => (state.mastFile = file),
  newMastFile: (state, file) => (state.mastFile = file)
};

export default {
  state,
  getters,
  actions,
  mutations
};
