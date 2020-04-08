import { AxiosBase } from "@/api/axios-base";
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
    return await AxiosBase.get(`mrp/bom-files/${file_id}/bom-items`)
      .then(response => {
        commit("setBomItems", response.data);
      });
  },
  // Agregar item
  addBomItems({ commit }, data) {
    return AxiosBase.post("mrp/bom-items/", data)
      .then(response => {
        if (response.data.length > 1) {
          commit("setBomItems", response.data);
        } else commit("newBomItem", response.data[0]);
      });
  },

  async updateBomItem({ commit }, item) {
    return await AxiosBase.put(`mrp/bom-items/${item.id}/`, item)
      .then(response => {
        commit("updatedBomItem", response.data);
      });
  },

  async deleteBomItem({ commit }, item) {
    return await AxiosBase.delete(`mrp/bom-items/${item.id}/`)
      .then(() => {
        commit("deletedBomItem", item);
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
