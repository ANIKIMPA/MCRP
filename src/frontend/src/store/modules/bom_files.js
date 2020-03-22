import { AxiosBase } from "@/api/axios-base";
import functions from "@/js/functions";

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
    return new Promise((resolve, reject) => {
      AxiosBase.get("mrp/bom-files/")
      .then(response => {
        commit("setBomFiles", response.data);
        resolve();
      })
      .catch(() => {
        reject()
      });
    })
  },

  async fetchBomFile({ commit }, file_id) {
    await AxiosBase.get(`mrp/bom-files/${file_id}/`)
      .then(response => {
        commit("setBomFile", response.data);
      })
      .catch(error => {
        commit(
          "throwError",
          error.response.data[Object.keys(error.response.data)[0]][0],
          { root: true }
        );
      });
  },

  createNewBomFile({ commit }, file) {
    AxiosBase.post("mrp/bom-files/", file)
      .then(response => {
        commit("newBomFile", response.data);
      })
      .catch(error => {
        commit(
          "throwError",
          error.response.data[Object.keys(error.response.data)[0]][0],
          { root: true }
        );
      });
  },

  async deleteBomFile({ commit }, file) {
    await AxiosBase.put(`mrp/bom-files/${file.id}/`, file)
      .then(() => {
        commit("deletedBomFile", file);
      })
      .catch(error => {
        commit(
          "throwError",
          error.response.data[Object.keys(error.response.data)[0]][0],
          { root: true }
        );
      });
  }
};

// Methods
const mutations = {
  // Set all files to state
  setBomFiles: (state, files) => state.allBomFiles = files,

  setBomFile: (state, file) => (state.bomFile = file),
  newBomFile: (state, file) => (state.bomFile = file),
  deletedBomFile: (state, file) => functions.remove(state.allBomFiles, file)
};

export default {
  state,
  getters,
  actions,
  mutations
};
