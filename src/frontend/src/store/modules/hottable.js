const state =  {
    hotData: null,
    hotSettings: {
      readOnly: false
    }
  }

const mutations = {
    updateData(state, hotData) {
      state.hotData = hotData;
    },
    updateSettings(state, updateObj) {
      state.hotSettings[updateObj.prop] = updateObj.value;
    }
  }

  export default {
    state,
    mutations
};