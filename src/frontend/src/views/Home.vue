<template>
  <b-container fluid class="bv-example-row bv-example-row-flex-cols py-2">
    <DataGrid />
  </b-container>
</template>

<script>
import DataGrid from "@/components/DataGrid";
export default {
  name: "home",
  components: {
    DataGrid
  }
};
</script>

<style scoped>
.h-200 {
  height: 200px;
  background-color: aqua;
}
</style>
