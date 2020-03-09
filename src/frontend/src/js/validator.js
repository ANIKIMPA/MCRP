const validator = {
  isPositive(value) {
    if (typeof value === "number" && value >= 0) {
      return true;
    } else {
      return false;
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
    if (typeof(value) !== "number" && (typeof(value) == "object" || value.trim() == "")) return false;
    else return true;
  },

  isNumeric(value) {
    if (typeof value === "number") {
      return true;
    } else {
      return false;
    }
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
