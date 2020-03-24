import store from "../store";

const functions = {
  remove(arr, elem) {
    let index = arr.indexOf(elem);
    if (index !== -1) arr.splice(index, 1);

    return arr;
  },

  handleError(error) {
    for (let value of Object.values(error.response.data)) {
      store.commit("throwError", value);
    }
  },

  convertPeriods(item) {
    let periods = item.periods.split(",");
    for (let i = 0; i < periods.length; i++) {
      item[`period${i + 1}`] = periods[i];
    }

    return item;
  },

  convertReceipts(item) {
    let receipts = item.receipts.split(",");
    for (let i = 0; i < receipts.length; i++) {
      item[`receipt${i + 1}`] = receipts[i];
    }

    return item;
  }
};

export default functions;
