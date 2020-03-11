import axios from "axios";
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
    await axios
      .get(`http://localhost:8000/api/v1.0/mrp/mast-files/${file_id}/mast-items`)
      .then(response => {
        commit("setMastItems", response.data);
      })
      .catch(error => {
        console.log(error)
        commit("throwError", error.response.data[Object.keys(error.response.data)[0]][0], { root: true });
      });
  },
  // Agregar item
  addMastItems({ commit }, data) {
    axios.post("http://localhost:8000/api/v1.0/mrp/mast-items/", data)
      .then(response => {
        if(response.data.length > 1)
          commit("setMastItems", response.data);
        else
          commit("newMastItem", response.data[0]);
      })
      .catch(error => {
        console.log(error)
        commit("throwError", error.response.data[Object.keys(error.response.data)[0]][0], { root: true });
      });
  },

  async updateMastItem({ commit }, item) {
    await axios
      .put(`http://localhost:8000/api/v1.0/mrp/mast-items/${item.id}/`, item)
      .then(response => {
        commit("updatedMastItem", response.data);
      })
      .catch(error => {
        console.log(error)
        commit("throwError", error.response.data[Object.keys(error.response.data)[0]][0], { root: true });
      });
  },

  async deleteMastItem({ commit }, item) {
    await axios
      .delete(`http://localhost:8000/api/v1.0/mrp/mast-items/${item.id}/`, item)
      .then(() => {
        commit("deletedMastItem", item);
      })
      .catch(error => {
        console.log(error)
        commit("throwError", error.response.data[Object.keys(error.response.data)[0]][0], { root: true });
      });
  }
};

const mutations = {
  // Set all mastItems to state
  setMastItems: (state, items) => state.mastItems = items.map(item => convertPeriods(item)),

  //Add item to state
  newMastItem: (state, item) => state.mastItems.push(convertPeriods(item)),
  
  // Update item in state
  updatedMastItem: (state, mastItem) => {
    const updItem = convertPeriods(mastItem);

    const index = state.mastItems.findIndex(item => item.id === updItem.id);
    if (index !== -1) {
      state.mastItems.splice(index, 1, updItem);
    }
  },
  // Delete item in state
  deletedMastItem: (state, mastItem) => functions.remove(state.mastItems, mastItem)
};

export default {
  state,
  getters,
  actions,
  mutations
};

function convertPeriods(item) {
  let periods = item.periods.split(",");
  for(let i=0; i<periods.length; i++) {
    item[`period${i + 1}`] = periods[i]
  }

  return item
}