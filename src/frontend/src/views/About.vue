<template>
  <div>    
  </div>
</template>

<script>
export default {
  data() {
    return {
      
    }
  },
  methods: {
    max(arr) {
      return this.maxHelper(arr, arr.length - 1);
    },
    maxHelper(arr, index) {
      if(index === 0) {
        return arr[0]
      } else {
        return Math.max(arr[index], this.maxHelper(arr, index - 1))
      }
    },

    sum(arr, index) {
      if(index === 0) {
        return arr[0]
      } else {
        return arr[index] + this.sum(arr, index - 1);
      }
    },

    pairs(arr, idx) {
      let pairs = []
      return this.pairsHelper(arr, idx, pairs)
    },
    pairsHelper(arr, idx, pairs) {
      if(idx < 0) {
        return pairs
      } else if(arr[idx] % 2 === 0) {
        pairs.push(arr[idx])
        return this.pairsHelper(arr, idx - 1, pairs) 
      } else {
        return this.pairsHelper(arr, idx - 1, pairs)
      }
    },

    main() {
      let numbers = [19, 23, 26, 12, 6, 2, 30, 3, 7, 0, 1]

      console.log(this.pairs(numbers, numbers.length - 1))
    }
  },
  mounted() {
    this.main();
  }
};
</script>

<style>
  .border-dark {
    border: #000000 solid 1px;
  }
</style>
