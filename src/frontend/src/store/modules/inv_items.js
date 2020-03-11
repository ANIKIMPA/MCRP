import axios from "axios";
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
    await axios
      .get(`http://localhost:8000/api/v1.0/mrp/inv-files/${file_id}/inv-items`)
      .then(response => {
        commit("setInvItems", response.data);
      })
      .catch(error => {
        console.log(error)
        commit("throwError", error.response.data[Object.keys(error.response.data)[0]][0], { root: true });
      });
  },

  async addInvItems({ commit }, data) {
    await axios
      .post("http://localhost:8000/api/v1.0/mrp/bom-items/", data)
      .then(response => {
        if(response.data.length > 1)
          commit("setInvItems", response.data);
        else
          commit("newInvItem", response.data[0]);
      })
      .catch(error => {
        console.log(error)
        commit("throwError", error.response.data[Object.keys(error.response.data)[0]][0], { root: true });
      });
  },

  async updateInvItem({ commit }, item) {
    await axios
      .put(`http://localhost:8000/api/v1.0/mrp/inv-items/${item.id}/`, item)
      .then(response => {
        commit("updatedInvItem", response.data);
      })
      .catch(error => {
        console.log(error)
        commit("throwError", error.response.data[Object.keys(error.response.data)[0]][0], { root: true });
      });
  },

  async deleteInvItem({ commit }, item) {
    await axios
      .delete(`http://localhost:8000/api/v1.0/mrp/inv-items/${item.id}/`, item)
      .then(() => {
        commit("deletedInvItem", item);
      })
      .catch(error => {
        console.log(error)
        commit("throwError", error.response.data[Object.keys(error.response.data)[0]][0], { root: true });
      });
  }
};

const mutations = {
  // Set all invItems to state
  setInvItems: (state, invItems) => state.invItems = invItems.map(item => convertReceipts(item)),

  //Add item to state
  newInvItem: (state, item) => state.invItems.push(convertReceipts(item)),

  // Update item in state
  updatedInvItem: (state, invItem) => {
    const updItem = convertReceipts(invItem)

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

function convertReceipts(item) {
  let receipts = item.receipts.split(",");
  for(let i=0; i<receipts.length; i++) {
    item[`receipt${i + 1}`] = receipts[i]
  }

  return item
}
