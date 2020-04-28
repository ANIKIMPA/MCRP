import axios from "axios"
import { AxiosBase } from "@/api/axios-base";

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
          reject(error.response.data);
        });
    });
  },
  logoutUser(context) {
    if (context.getters.loggedIn) {
      return new Promise((resolve) => {
        // AxiosBase
        //   .post("logout/", {
        //     "refresh_token": localStorage.getItem("refresh_token")
        //   })
        //   .then(() => {
        //     localStorage.removeItem("access_token");
        //     localStorage.removeItem("refresh_token");
        //     context.commit("destroyToken", { root: true });
        //     resolve();
        //   })
        //   .catch(() => {
            localStorage.removeItem("access_token");
            localStorage.removeItem("refresh_token");
            context.commit("destroyToken", { root: true });
            resolve();
          // });
      });
    }
  },
  loginUser({ commit }, credentials) {
    return new Promise((resolve, reject) => {
      // send the username and password to the backend API:
      axios
        .post("http://localhost:8000/api/v1.0/login/", credentials)
        //if successful update local storage:
        .then(response => {
          commit("updateLocalStorage", response.data, { root: true }); // store the access and refresh token in localstorage
          resolve();    
        })
        .catch(error => {
          reject(error.response.data);
        });
    });
  },

  fetchUserProfile({commit}) {
    AxiosBase.get("profile/").then((response) => {
      commit("setUser", response.data);
    }).catch(() => {
    })
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
