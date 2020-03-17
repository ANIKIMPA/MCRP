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
    await AxiosBase
      .get(`http://localhost:8000/api/v1.0/mrp/item-master-files/${file_id}/items-masters`)
      .then(response => {
        commit("setItemsMasters", response.data);
      })
      .catch(error => {
        for (let value of Object.values(error.response.data)) {
          commit("throwError", value, { root: true });
        }
      });
  },
  // Agregar item
  addItemsMasters({ commit }, data) {
    AxiosBase
      .post("http://localhost:8000/api/v1.0/mrp/items-masters/", data)
      .then(response => {
        if(response.data.length > 1)
          commit("setItemsMasters", response.data);
        else
          commit("newItemMaster", response.data[0]);
      })
      .catch(error => {
        for (let value of Object.values(error.response.data)) {
          commit("throwError", value, { root: true });
        }
      });
  },

  async updateItemMaster({ commit }, item) {
    await AxiosBase
      .put(`http://localhost:8000/api/v1.0/mrp/items-masters/${item.id}/`, item)
      .then(response => {
        commit("updatedItemMaster", response.data);
      })
      .catch(error => {
        for (let value of Object.values(error.response.data)) {
          commit("throwError", value, { root: true });
        }
      });
  },

  async deleteItemMaster({ commit }, item) {
    await AxiosBase
      .delete(`http://localhost:8000/api/v1.0/mrp/items-masters/${item.id}/`, item)
      .then(() => {
        commit("deletedItemMaster", item);
      })
      .catch(error => {
        for (let value of Object.values(error.response.data)) {
          commit("throwError", value, { root: true });
        }
      });
  }
};

const mutations = {
  // Set all itemsMasters to state
  setItemsMasters: (state, itemsMasters) => state.itemsMasters = itemsMasters,

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