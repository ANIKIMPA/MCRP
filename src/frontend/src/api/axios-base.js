import axios from "axios";
import store from "../store";
import functions from "../js/functions";
const APIUrl = "http://localhost:8000/api/v1.0/";

class AxiosBase {
  static config() {
    return {
      headers: {
        Authorization: `Bearer ${localStorage.getItem("access_token")}`,
        'Content-Type': 'application/json'
      }
    };
  }

  static post(url, params) {
    return new Promise((resolve, reject) => {
      axios
        .post(APIUrl + url, params, AxiosBase.config())
        .then(response => {
          resolve(response);
        })
        .catch(error => {
          functions.handleError(error)
          AxiosBase.getApi(error);
          reject(error);
        });
    });
  }

  static get(url) {
    return new Promise((resolve, reject) => {
      axios
        .get(APIUrl + url, AxiosBase.config())
        .then(response => {
          resolve(response);
        })
        .catch(error => {
          functions.handleError(error)
          AxiosBase.getApi(error);
          reject(error);
        });
    });
  }

  static put(url, params) {
    return new Promise((resolve, reject) => {
      axios
        .put(APIUrl + url, params, AxiosBase.config())
        .then(response => {
          resolve(response);
        })
        .catch(error => {
          functions.handleError(error)
          AxiosBase.getApi(error);
          reject(error);
        });
    });
  }

  static delete(url) {
    return new Promise((resolve, reject) => {
      axios
        .delete(APIUrl + url, AxiosBase.config())
        .then(response => {
          resolve(response);
        })
        .catch(error => {
          functions.handleError(error)
          AxiosBase.getApi(error);
          reject(error);
        });
    });
  }

  static getApi(err) {
    // if error response status is 401, it means the request was invalid due to expired access token
    if (err.config && err.response && err.response.status === 401) {
      store
        .dispatch("refreshToken") // attempt to obtain new access token by running 'refreshToken' action
        .then(access => {
          // if successful re-send the request to get the data from server
          axios
            .request({
              baseURL: APIUrl,
              method: "get",
              headers: { Authorization: `Bearer ${access}` }, // the new access token is attached to the authorization header
              url: "/api/v1.0/"
            })
            .then(response => {
              // if successfully received the data store it in store.state.APIData so that 'Downloads' component can grab the
              // data from it and display to the client.
              store.state.APIData = response.data;
            })
            .catch(err => {
              return Promise.reject(err);
            });
        })
        .catch(err => {
          return Promise.reject(err);
        });
    }
  }
}

const axiosBase = axios.create({
  baseURL: APIUrl,
  headers: { contentType: "application/json" }
});
const getAPI = axios.create({
  baseURL: APIUrl
});
getAPI.interceptors.response.use(undefined, function(err) {
  // if error response status is 401, it means the request was invalid due to expired access token
  if (err.config && err.response && err.response.status === 401) {
    store
      .dispatch("refreshToken") // attempt to obtain new access token by running 'refreshToken' action
      .then(access => {
        // if successful re-send the request to get the data from server
        axios
          .request({
            baseURL: APIUrl,
            method: "get",
            headers: { Authorization: `Bearer ${access}` }, // the new access token is attached to the authorization header
            url: "/api/v1.0/"
          })
          .then(response => {
            // if successfully received the data store it in store.state.APIData so that 'Downloads' component can grab the
            // data from it and display to the client.
            store.state.APIData = response.data;
          })
          .catch(err => {
            return Promise.reject(err);
          });
      })
      .catch(err => {
        return Promise.reject(err);
      });
  }
});

export { AxiosBase, axiosBase, getAPI };
