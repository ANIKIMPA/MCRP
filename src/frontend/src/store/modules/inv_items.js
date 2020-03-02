import axios from "axios";

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
        console.log(error);
        commit("throwError", error.response.data[Object.keys(error.response.data)[0]][0], { root: true });
      });
  },
  // Agregar item
  addInvItem({ commit }, item) {
    axios
      .post("http://localhost:8000/api/v1.0/mrp/inv-items/", item)
      .then(response => {
        commit("newInvItem", response.data);
      })
      .catch(error => {
        console.log(error);
        commit("throwError", error.response.data[Object.keys(error.response.data)[0]][0], { root: true });
      });
  },

  async updateInvItem({ commit }, item) {
    await axios
      .put(`http://localhost:8000/api/v1.0/mrp/inv-items/${item.id}/`, item)
      .then(response => {
        commit("updateInvItem", response.data);
      })
      .catch(error => {
        console.log(error);
        commit("throwError", error.response.data[Object.keys(error.response.data)[0]][0], { root: true });
      });
  }
};

const mutations = {
  // Set all invItems to state
  updateInvItems: (state, invItems) => (state.invItems = invItems),
  setInvItems: (state, invItems) => (state.invItems = invItems),

  //Add item to state
  newInvItem: (state, item) => state.invItems.push(item),

  // Update item in state
  updateInvItem: (state, updItem) => {
    const index = state.invItems.findIndex(item => item.id === updItem.id);
    if (index !== -1) {
      state.invItems.splice(index, 1, updItem);
    }
  }
};

export default {
  state,
  getters,
  actions,
  mutations
};
