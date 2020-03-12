const state = {
  error: "",
  info: ""
};

const getters = {
  getError: state => state.error,
  getInfo: state => state.info,
};

const mutations = {
	// Set error to state
  throwError: (state, errorMsg) => state.error = errorMsg,
  showInfo: (state, errorMsg) => state.error = errorMsg
};

export default {
  state,
  getters,
  mutations
};
