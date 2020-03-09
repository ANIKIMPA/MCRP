const validator = {
  isPositive(value, callback) {
    if (typeof value === "number") {
      callback(value >= 0);
    } else {
      callback(false);
    }
  },

  isValidPercent(value, callback) {
    if (typeof value === "number") {
      callback(value >= 0 && value <= 1);
    } else {
      callback(false);
    }
  },

  isNotEmpty(value) {
    if (!value || value.trim() == "") return false;
    else return true;
  },

  allRowsSelected() {
    // Disable option when attempt to remove all rows
    const selected = this.getSelectedLast();
    let periodsQty = this.countVisibleRows();
    let selectedQty = selected[2] - selected[0];
    selectedQty = selectedQty > 0 ? selectedQty + 1 : selectedQty * -1 + 1;
    return selectedQty >= periodsQty;
  }
};

export default validator;
