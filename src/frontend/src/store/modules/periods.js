import axios from "axios";

const state = {
  periods: []
};

const getters = {
  getAllPeriods: state => state.periods
};

const actions = {
  // Obtener lista de periods
  async fetchPeriods({ commit }, file_id) {
    await axios
      .get(`http://localhost:8000/api/v1.0/mrp/mast-files/${file_id}/periods`)
      .then(response => {
        commit("updatePeriods", response.data);
      })
      .catch(error => {
        console.log(error);
      });
  },
  // Agregar period
  addPeriod({ commit }, period) {
    axios
      .post("http://localhost:8000/api/v1.0/mrp/periods/", period)
      .then(response => {
        commit("newPeriod", response.data);
      })
      .catch(error => {
        console.log(error);
      });
  },

  async updatePeriod({ commit }, period) {
    await axios
      .put(`http://localhost:8000/api/v1.0/mrp/periods/${period.id}/`, period)
      .then(response => {
        commit("updatePeriod", response.data);
      })
      .catch(error => {
        console.log(error);
      });
  }
};

const mutations = {
  // Set all periods to state
  updatePeriods: (state, periods) => {
    for (let i = 0; i < periods.length; i++) {
      createNeWPeriod(state, periods[i])
    }
  },

  //Add period to state
  newPeriod: (state, period) => {
    createNeWPeriod(state, period)
  },

  // Update period in state
  updatePeriod: (state, updPeriod) => {
    const index = state.periods.findIndex(period => period.id === updPeriod.id);
    if (index !== -1) {
      state.periods.splice(index, 1, updPeriod);
    }
  }
};

export default {
  state,
  getters,
  actions,
  mutations
};


function createNeWPeriod(state, period) {
  let idx = state.periods.findIndex(
    mast => mast.part_number == period.part_number
  );

  if (idx >= 0) {
    state.periods[idx][`period${period.order}`] = null;
  } else {
    period[`period${period.order}`] = null;
    state.periods.push({ ...period });
  }
}