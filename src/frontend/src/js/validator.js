const validator = {
    isPositive(value, callback) {
        if (typeof (value) === "number") {
            callback(value >= 0)
        }
        else {
            callback(false)
        }
    },

    isValidPercent(value, callback) {
        if (typeof (value) === "number") {
            callback(value >= 0 && value <= 1)
        }
        else {
            callback(false)
        }
    },

    isNotEmpty(value, callback) {
        if (!value || value.trim() == "")
            callback(false)
        else
            callback(true)
    }
}

export default validator