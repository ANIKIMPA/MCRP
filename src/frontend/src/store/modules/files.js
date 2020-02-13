import axios from 'axios';

const state = {
    files: [],
    fileSelected: {}
};

const getters = {
    allFiles: (state) => state.files,
    getFirstFile: (state) => state.files[0],
};

const actions = {
    // Obtener lista de files
    async fetchFiles({ commit }) {
        await axios.get("http://localhost:8000/api/v1.0/files/").then((response) => {
            commit('setFiles', response.data);
        })
        .catch((error) => {
            console.log(error)
        });
    },
    // Agregar file
    createNewFile({ commit }, file) {
        axios.post("http://localhost:8000/api/v1.0/files/", file).then((response) => {
            commit("newFile", response.data)
        })
        .catch((error) => {
            console.log(error)
        });
    },

    async updateFile({ commit }, file) {
      await axios.put(`http://localhost:8000/api/v1.0/files/${file.id}/`, file).then((response) => {
          commit('updateFile', response.data);
      })
      .catch((error) => {
          console.log(error);
      })
    },
};

const mutations = {
  // Set all files to state
  setFiles: (state, files) => (state.files = files),

  // Set file selected to state
  setFile: (state, file) => (state.fileSelected = file),

  //Add file to state
  newFile: (state, file) => state.files.unshift(file),

  // Update file in state
  updateFile: (state, updFile) => {
    const index = state.files.findIndex(file => file.id === updFile.id);
    if (index !== -1) {
      state.files.splice(index, 1, updFile);
    }
  }
};

export default {
    state,
    getters,
    actions,
    mutations
};