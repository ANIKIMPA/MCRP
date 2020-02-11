<template lang="html">
    <b-container>
        <AddItem/>
        <h3>Items</h3>

        <div class="items">
            <div v-for="item in allItems" :key="item.id" class="item">
                <div>Part Number: {{ item.part_number }}</div>
                <div>Type: {{ item.tipo }}</div>
                <div>Parent: {{ item.parent }}</div>
                <div>Qty: {{ item.qty }}</div>
            </div>
        </div>
    </b-container>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';
import AddItem from '@/components/AddItem.vue';

export default {
    name: "items",
    components: { AddItem },
    methods: {
        ...mapActions(['fetchItems']),
    },
    computed: mapGetters(['allItems']),
    created() {
        this.fetchItems();
    }
}
</script>

<style lang="css" scoped>
.items {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-gap: 1rem;
}
.item {
  border: 1px solid #ccc;
  background: #41b883;
  padding: 1rem;
  border-radius: 5px;
  text-align: center;
  position: relative;
  cursor: pointer;
}
i {
  position: absolute;
  bottom: 10px;
  right: 10px;
  color: #fff;
  cursor: pointer;
}
.legend {
  display: flex;
  justify-content: space-around;
  margin-bottom: 1rem;
}
.complete-box {
  display: inline-block;
  width: 10px;
  height: 10px;
  background: #35495e;
}
.incomplete-box {
  display: inline-block;
  width: 10px;
  height: 10px;
  background: #41b883;
}
.is-complete {
  background: #35495e;
  color: #fff;
}
@media (max-width: 500px) {
  .items {
    grid-template-columns: 1fr;
  }
}
</style>