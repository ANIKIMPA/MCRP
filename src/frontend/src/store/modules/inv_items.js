import { AxiosBase } from "@/api/axios-base";
import functions from "@/js/functions";

const state = {
  invItems: []
};

const getters = {
  getAllInvItems: state => state.invItems
};

const actions = {
  // Obtener lista de invItems
  async fetchInvItems({ commit }, file_id) {
    await AxiosBase.get(`mrp/inv-files/${file_id}/inv-items`).then(response => {
      commit("setInvItems", response.data);
    });
  },

  async addInvItems({ commit }, data) {
    await AxiosBase.post("mrp/inv-items/", data).then(response => {
      if (response.data.length > 1) commit("setInvItems", response.data);
      else commit("newInvItem", response.data[0]);
    });
  },

  async updateInvItem({ commit }, item) {
    await AxiosBase.put(`mrp/inv-items/${item.id}/`, item).then(response => {
      commit("updatedInvItem", response.data);
    });
  },

  async deleteInvItem({ commit }, item) {
    await AxiosBase.delete(`mrp/inv-items/${item.id}/`, item).then(() => {
      commit("deletedInvItem", item);
    });
  }
};

const mutations = {
  // Set all invItems to state
  setInvItems: (state, invItems) =>
    (state.invItems = invItems.map(item => functions.convertReceipts(item))),

  //Add item to state
  newInvItem: (state, item) => state.invItems.push(functions.convertReceipts(item)),

  // Update item in state
  updatedInvItem: (state, invItem) => {
    const updItem = functions.convertReceipts(invItem);

    const index = state.invItems.findIndex(item => item.id === updItem.id);
    if (index !== -1) {
      state.invItems.splice(index, 1, updItem);
    }
  },
  // Delete item in state
  deletedInvItem: (state, invItem) => functions.remove(state.invItems, invItem)
};

export default {
  state,
  getters,
  actions,
  mutations
};
