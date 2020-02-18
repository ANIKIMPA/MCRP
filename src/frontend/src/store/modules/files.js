import axios from "axios";

// Computed
const state = {
  allFiles: [],
  files: {
    bomFile: {
      title: "",
      tipo: ""
    },
    mastFile: {
      title: "",
      tipo: ""
    }
  }
};

// Computed
const getters = {
  allFiles: state => state.allFiles,
  bomFile: state => state.files.bomFile,
  mastFile: state => state.files.mastFile
};

// Methods
const actions = {
  // Obtener lista de files
  async fetchFiles({ commit }) {
    await axios
      .get("http://localhost:8000/api/v1.0/mrp/files/")
      .then(response => {
        commit("setFiles", response.data);
      })
      .catch(error => {
        console.log(error);
      });
  },
  // Agregar file
  createNewBomFile({ commit }, file) {
    axios
      .post("http://localhost:8000/api/v1.0/mrp/files/", file)
      .then(response => {
        commit("newBomFile", response.data);
      })
      .catch(error => {
        console.log(error);
      });
  },
  createNewMastFile({ commit }, file) {
    axios
      .post("http://localhost:8000/api/v1.0/mrp/files/", file)
      .then(response => {
        commit("setMastFile", response.data);
      })
      .catch(error => {
        console.log(error);
      });
  }
};

// Methods
const mutations = {
  // Set all files to state
  setFiles: (state, files) => (state.allFiles = files),

  //Add file to state
  newBomFile: (state, file) => (state.files.bomFile = file),
  setBomFile: (state, file) => (state.files.bomFile = file),
  setMastFile: (state, file) => (state.files.mastFile = file)
};

export default {
  state,
  getters,
  actions,
  mutations
};
