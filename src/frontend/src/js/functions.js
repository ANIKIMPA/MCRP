import store from "../store";

const functions = {
    remove(arr, elem) {
        let index = arr.indexOf(elem)
        if(index !== -1)
            arr.splice(index, 1)
        
        return arr
    },
    
    handleError(error) {
        for (let value of Object.values(error.response.data)) {
            store.commit("throwError", value);
        }
    }
}

export default functions