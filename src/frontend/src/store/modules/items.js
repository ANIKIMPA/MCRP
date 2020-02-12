import axios from 'axios';

const state = {
    items: []
};

const getters = {
    getAllItems: (state) => state.items
};

const actions = {
    // Obtener lista de items
    async fetchItems({ commit }) {
        await axios.get("http://localhost:8000/api/v1.0/items/").then((response) => {
            commit('updateItems', response.data);
        })
        .catch((error) => {
            console.log(error)
        });
    },
    // Agregar item
    addItem({ commit }, item) {
        axios.post("http://localhost:8000/api/v1.0/items/", item).then((response) => {
            commit("newItem", response.data)
        })
        .catch((error) => {
            console.log(error)
        });
    },

    async updateItem({ commit }, item) {
      await axios.put(`http://localhost:8000/api/v1.0/items/${item.id}/`, item).then((response) => {
          commit('updateItem', response.data);
      })
      .catch((error) => {
          console.log(error);
      })
    },
};

const mutations = {
  // Set all items to state
  updateItems: (state, items) => (state.items = items),

  //Add item to state
  newItem: (state, item) => state.items.push(item),

  // Update item in state
  updateItem: (state, updItem) => {
    const index = state.items.findIndex(item => item.id === updItem.id);
    if (index !== -1) {
      state.items.splice(index, 1, updItem);
    }
  }
};

export default {
    state,
    getters,
    actions,
    mutations
};