import { AxiosBase } from "@/api/axios-base";
import functions from "@/js/functions";

const state = {
  itemsMasters: []
};

const getters = {
  getAllItemsMasters: state => state.itemsMasters
};

const actions = {
  // Obtener lista de itemsMasters
  async fetchItemsMasters({ commit }, file_id) {
    return await AxiosBase.get(`mrp/item-master-files/${file_id}/items-masters`).then(
      response => {
        commit("setItemsMasters", response.data);
      }
    );
  },
  // Agregar item
  addItemsMasters({ commit }, data) {
    return AxiosBase.post("mrp/items-masters/", data).then(response => {
          if (response.data.length > 1) commit("setItemsMasters", response.data);
          else commit("newItemMaster", response.data[0]);
      })
  },

  async updateItemMaster({ commit }, item) {
    return await AxiosBase.put(`mrp/items-masters/${item.id}/`, item).then(
      response => {
        commit("updatedItemMaster", response.data);
      }
    );
  },

  async deleteItemMaster({ commit }, item) {
    return await AxiosBase.delete(`mrp/items-masters/${item.id}/`, item).then(() => {
      commit("deletedItemMaster", item);
    });
  }
};

const mutations = {
  // Set all itemsMasters to state
  setItemsMasters: (state, itemsMasters) => (state.itemsMasters = itemsMasters),

  //Add item to state
  newItemMaster: (state, item) => state.itemsMasters.push(item),
  // Update item in state
  updatedItemMaster: (state, updItem) => {
    const index = state.itemsMasters.findIndex(item => item.id === updItem.id);
    if (index !== -1) {
      state.itemsMasters.splice(index, 1, updItem);
    }
  },

  deletedItemMaster: (state, item) => functions.remove(state.itemsMasters, item)
};

export default {
  state,
  getters,
  actions,
  mutations
};
