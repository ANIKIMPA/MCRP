import axios from "axios";

const state = {
  periods: [],
  convertedPeriods: []
};

const getters = {
  getAllPeriods: state => state.periods,
  getAllConvertedPeriods: state => state.convertedPeriods
};

const actions = {
  // Obtener lista de periods
  async fetchPeriods({ commit }, file_id) {
    await axios
      .get(`http://localhost:8000/api/v1.0/mrp/mast-files/${file_id}/periods`)
      .then(response => {
        commit("setPeriods", response.data);
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
    state.periods = periods

    for (let i = 0; i < periods.length; i++) {
      convertPeriod(state, periods[i])
    }
  },
  setPeriods: (state, periods) => {
    state.periods = [...periods]
    state.convertedPeriods = []

    for (let i = 0; i < periods.length; i++) {
      convertPeriod(state, periods[i])
    }
  },

  //Add period to state
  newPeriod: (state, period) => {
    state.periods.push(period)
    convertPeriod(state, period)
  },

  // Update period in state
  updatePeriod: (state, updPeriod) => {
    const index = state.periods.findIndex(period => period.id === updPeriod.id);
    if (index !== -1) {
      state.periods.splice(index, 1, updPeriod);
    }


    // Update converted period
    let idx = state.convertedPeriods.findIndex(
      mast => mast.part_number == updPeriod.part_number
    );
  
    if (idx >= 0) {
      state.convertedPeriods[idx][`period${updPeriod.order}`] = updPeriod.data;
    } else {
      updPeriod[`period${updPeriod.order}`] = updPeriod.data;
      state.convertedPeriods.splice(idx, 1, { ...updPeriod });
    }
  }
};

export default {
  state,
  getters,
  actions,
  mutations
};


function convertPeriod(state, period) {
  let idx = state.convertedPeriods.findIndex(
    mast => mast.part_number == period.part_number
  );

  if (idx >= 0) {
    state.convertedPeriods[idx][`${period.id}`] = period.data;
  } else {
    period[`${period.id}`] = period.data;
    state.convertedPeriods.push({ ...period });
  }
}