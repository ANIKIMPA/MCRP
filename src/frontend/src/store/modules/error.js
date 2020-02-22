const state = {
  error: ""
};

const getters = {
  getError: state => state.error
};

const mutations = {
	// Set error to state
  throwError: (state, errorMsg) => state.error = errorMsg
};

export default {
  state,
  getters,
  mutations
};
