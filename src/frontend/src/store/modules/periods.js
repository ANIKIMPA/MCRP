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
        commit("throwError", error.response.data[Object.keys(error.response.data)[0]][0], { root: true });
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
        commit("throwError", error.response.data[Object.keys(error.response.data)[0]][0], { root: true });
      });
  },

  async updatePeriod({ state, commit }, params) {
    console.log(params);
    const part_number = state.convertedPeriods[params.row].part_number;
    const mPeriod = state.periods.find(
      mPeriod =>
        mPeriod.part_number == part_number && mPeriod.order == params.prop
    );
    mPeriod.data = params.newValue;

    await axios
      .put(`http://localhost:8000/api/v1.0/mrp/periods/${mPeriod.id}/`, mPeriod)
      .then(response => {
        commit("updatedPeriod", response.data);
      })
      .catch(error => {
        console.log(error);
        commit("throwError", error.response.data[Object.keys(error.response.data)[0]][0], { root: true });
      });
  },

  async updatePeriodsPartNumber({ commit }, params) {
    let mPeriods = state.periods.filter(
      mPeriod => mPeriod.part_number == params.oldValue
    );
    for (let i = 0; i < mPeriods.length; i++) {
      mPeriods[i].part_number = params.newValue;

      await axios
        .put(
          `http://localhost:8000/api/v1.0/mrp/periods/${mPeriods[i].id}/`,
          mPeriods[i]
        )
        .then(response => {
          commit("updatedPeriod", response.data);
        })
        .catch(error => {
          console.log(error);
          commit("throwError", error.response.data[Object.keys(error.response.data)[0]][0], { root: true });
        });
    }
  }
};

const mutations = {
  // Set all periods to state
  updatePeriods: (state, periods) => {
    state.periods = periods;

    for (let i = 0; i < periods.length; i++) {
      convertPeriod(state, periods[i]);
    }
  },
  setPeriods: (state, periods) => {
    state.periods = [...periods];
    state.convertedPeriods = [];

    for (let i = 0; i < periods.length; i++) {
      convertPeriod(state, periods[i]);
    }
  },

  //Add period to state
  newPeriod: (state, period) => {
    state.periods.push(period);
    convertPeriod(state, period);
  },

  // Update period in state
  updatedPeriod: (state, updPeriod) => {
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
    state.convertedPeriods[idx][`${period.order}`] = period.data;
  } else {
    period[`${period.order}`] = period.data;
    state.convertedPeriods.push({ ...period });
  }
}
