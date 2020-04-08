import { AxiosBase } from "@/api/axios-base";
import functions from "@/js/functions";

const state = {
  mastItems: []
};

const getters = {
  getAllMastItems: state => state.mastItems
};

const actions = {
  // Obtener lista de mastItems
  async fetchMastItems({ commit }, file_id) {
    return await AxiosBase.get(`mrp/mast-files/${file_id}/mast-items`).then(response => {
      commit("setMastItems", response.data);
    });
  },
  // Agregar item
  addMastItems({ commit }, data) {
    return AxiosBase.post("mrp/mast-items/", data).then(response => {
      if (response.data.length > 1) commit("setMastItems", response.data);
      else commit("newMastItem", response.data[0]);
    });
  },

  async updateMastItem({ commit }, item) {
    return await AxiosBase.put(`mrp/mast-items/${item.id}/`, item).then(response => {
      commit("updatedMastItem", response.data);
    });
  },

  async deleteMastItem({ commit }, item) {
    return await AxiosBase.delete(`mrp/mast-items/${item.id}/`, item).then(() => {
      commit("deletedMastItem", item);
    });
  }
};

const mutations = {
  // Set all mastItems to state
  setMastItems: (state, items) =>
    (state.mastItems = items.map(item => functions.convertPeriods(item))),

  //Add item to state
  newMastItem: (state, item) => state.mastItems.push(functions.convertPeriods(item)),

  // Update item in state
  updatedMastItem: (state, mastItem) => {
    const updItem = functions.convertPeriods(mastItem);

    const index = state.mastItems.findIndex(item => item.id === updItem.id);
    if (index !== -1) {
      state.mastItems.splice(index, 1, updItem);
    }
  },
  // Delete item in state
  deletedMastItem: (state, mastItem) =>
    functions.remove(state.mastItems, mastItem)
};

export default {
  state,
  getters,
  actions,
  mutations
};
