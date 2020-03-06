const functions = {
    remove(arr, elem) {
        let index = arr.indexOf(elem)
        if(index !== -1)
            arr.splice(index, 1)
        
        return arr
    },
}

export default functions