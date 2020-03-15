import { axiosBase } from "@/api/axios-base";
import axios from "axios"

const state = {
  user: {}
};

const getters = {
  getUser: state => state.user
};

const actions = {
  registerUser({ commit }, data) {
    return new Promise((resolve, reject) => {
      axios
        .post("http://localhost:8000/api/v1.0/register/", data)
        .then(response => {
          commit
          resolve(response);
        })
        .catch(error => {
          console.log(error.response)
          reject(error.response.data);
        });
    });
  },
  logoutUser(context) {
    if (context.getters.loggedIn) {
      return new Promise((resolve) => {
        axiosBase
          .post("/logout/")
          .then(response => {
						context.commit("setUser", response.data);
            localStorage.removeItem("access_token");
            localStorage.removeItem("refresh_token");
            context.commit("destroyToken");
          })
          .catch(error => {
            localStorage.removeItem("access_token");
            localStorage.removeItem("refresh_token");
            context.commit("destroyToken");
            resolve(error);
          });
      });
    }
  },
  loginUser({ commit }, credentials) {
    return new Promise((resolve, reject) => {
      // send the username and password to the backend API:
      axios
        .post("http://localhost:8000/api/token/", credentials)
        //if successful update local storage:
        .then(response => {
          console.log(response.data)
          commit("updateLocalStorage", response.data, { root: true }); // store the access and refresh token in localstorage
          resolve();
        })
        .catch(error => {
          reject(error.response.data);
        });
    });
  }
};

const mutations = {
  setUser: (state, user) => state.user = user,
};

export default {
  state,
  getters,
  actions,
  mutations
};
