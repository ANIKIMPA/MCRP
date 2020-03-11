import axios from "axios";
import functions from "@/js/functions";

const state = {
  bomItems: []
};

const getters = {
  getAllBomItems: state => state.bomItems,
  getParentItems: state => state.bomItems.filter(item => item.parent == null)
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
        console.log(error)
        commit("throwError", error.response.data[Object.keys(error.response.data)[0]][0], { root: true });
      });
  },
  // Agregar item
  addBomItems({ commit }, data) {
    axios
      .post("http://localhost:8000/api/v1.0/mrp/bom-items/", data)
      .then(response => {
        if(response.data.length > 1)
          commit("setBomItems", response.data);
        else
          commit("newBomItem", response.data[0]);
      })
      .catch(error => {
        console.log(error)
        commit("throwError", error.response.data[Object.keys(error.response.data)[0]][0], { root: true });
      });
  },

  async updateBomItem({ commit }, item) {
    await axios
      .put(`http://localhost:8000/api/v1.0/mrp/bom-items/${item.id}/`, item)
      .then(response => {
        commit("updatedBomItem", response.data);
      })
      .catch(error => {
        console.log(error)
        commit("throwError", error.response.data[Object.keys(error.response.data)[0]][0], { root: true });
      });
  },

  async deleteBomItem({ commit }, item) {
    await axios
      .delete(`http://localhost:8000/api/v1.0/mrp/bom-items/${item.id}/`, item)
      .then(() => {
        commit("deletedBomItem", item);
      })
      .catch(error => {
        console.log(error)
        commit("throwError", error.response.data[Object.keys(error.response.data)[0]][0], { root: true });
      });
  }
};

const mutations = {
  // Set all bomItems to state
  setBomItems: (state, bomItems) => (state.bomItems = bomItems),

  //Add item to state
  newBomItem: (state, item) => state.bomItems.push(item),

  // Update item in state
  updatedBomItem: (state, updItem) => {
    const index = state.bomItems.findIndex(item => item.id === updItem.id);
    if (index !== -1) {
      state.bomItems.splice(index, 1, updItem);
    }
  },

  deletedBomItem: (state, item) => functions.remove(state.bomItems, item)
};

export default {
  state,
  getters,
  actions,
  mutations
};
