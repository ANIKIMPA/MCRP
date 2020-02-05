<template>
  <div id="app-4">
    <br><br>
    <span>Seleccionado: {{ selected }}</span>
    <br><br>
    <p class="mb-2">Select module for new data:</p>

    <b-list-group class="overflow-auto mh-300" ref="listado">
        <b-list-group-item :key="option.id" button v-for="option in options" @click="selected = option.id">
          {{ option.text }}
        </b-list-group-item>
    </b-list-group>

    <br><br>
    <1b-button @click="saludar">Click</1  b-button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      selected: "",
      options: [
        { text: 'Assigment', id: 1 },
        { text: 'Decission Analysis', id: 2 },
        { text: 'Decission Trees', id: 3 },
        { text: 'Material Requirement Planning', id: 4 }
      ]
    };
  },
  methods: {
    saludar() {
      console.log(this.$refs.listado.childElementCount);
    }
  }
};
</script>

<style>
</style>
