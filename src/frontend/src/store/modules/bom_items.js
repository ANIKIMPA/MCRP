import axios from "axios";

const state = {
  bomItems: []
};

const getters = {
  getAllBomItems: state => state.bomItems,
  getMasterItems: state => state.bomItems.filter(item => item.parent == null)
};

const actions = {
  // Obtener lista de bomItems
  async fetchBomItems({ commit }, file_id) {
    await axios
      .get(`http://localhost:8000/api/v1.0/mrp/bom-files/${file_id}/bom-items`)
      .then(response => {
        commit("setBomItems", response.data);
      })
      .catch(error => {
        console.log(error);
        commit("throwError", error.response.data[Object.keys(error.response.data)[0]][0], { root: true });
      });
  },
  // Agregar item
  addBomItem({ commit }, item) {
    axios
      .post("http://localhost:8000/api/v1.0/mrp/bom-items/", item)
      .then(response => {
        commit("newBomItem", response.data);
      })
      .catch(error => {
        console.log(error);
        commit("throwError", error.response.data[Object.keys(error.response.data)[0]][0], { root: true });
      });
  },

  async updateBomItem({ commit }, item) {
    await axios
      .put(`http://localhost:8000/api/v1.0/mrp/bom-items/${item.id}/`, item)
      .then(response => {
        commit("updateBomItem", response.data);
      })
      .catch(error => {
        console.log(error);
        commit("throwError", error.response.data[Object.keys(error.response.data)[0]][0], { root: true });
      });
  }
};

const mutations = {
  // Set all bomItems to state
  updateBomItems: (state, bomItems) => (state.bomItems = bomItems),
  setBomItems: (state, bomItems) => (state.bomItems = bomItems),

  //Add item to state
  newBomItem: (state, item) => state.bomItems.push(item),

  // Update item in state
  updateBomItem: (state, updItem) => {
    const index = state.bomItems.findIndex(item => item.id === updItem.id);
    if (index !== -1) {
      state.bomItems.splice(index, 1, updItem);
    }
  }
};

export default {
  state,
  getters,
  actions,
  mutations
};
