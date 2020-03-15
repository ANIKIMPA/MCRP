import { axiosBase } from "@/api/axios-base";

const state = {
  APIData: ""
};

const getters = {
  loggedIn: (state) =>  state.accessToken != null,
  accessToken: () => localStorage.getItem("access_token") || null,
  refreshToken: () => localStorage.getItem("refresh_token") || null
};

const actions = {
  refreshToken(context) {
    return new Promise((resolve, reject) => {
      axiosBase
        .post("/api/token/refresh/", {
          refresh: context.state.refreshToken
        }) // send the stored refresh token to the backend API
        .then(response => {
          // if API sends back new access and refresh token update the store
          console.log("New access successfully generated");
          context.commit("updateAccess", response.data.access);
          resolve(response.data.access);
        })
        .catch(err => {
          console.log("error in refreshToken Task");
          reject(err); // error generating new access and refresh token because refresh token has expired
        });
    });
  }
};

const mutations = {
  updateLocalStorage(state, token) {
    localStorage.setItem("access_token", token.access);
    localStorage.setItem("refresh_token", token.refresh);
    state.accessToken = token.access;
    state.refreshToken = token.refresh;
  },
  updateAccess(state, access) {
    state.accessToken = access;
  },
  destroyToken(state) {
    state.accessToken = null;
    state.refreshToken = null;
  }
};

export default {
  state,
  getters,
  actions,
  mutations
};
