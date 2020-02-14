<template>
  <div id="example1">
    <div id="example-preview" class="hot">
      <div id="toggle-boxes">
        <input v-on:click="toggleReadOnly" checked id="readOnlyCheck" type="checkbox" /><label for="readOnlyCheck"> Toggle <code>readOnly</code> for the entire table</label>
      </div>
      <hot-table ref="wrapper" :settings="hotSettings"></hot-table>
    </div>
    <div id="vuex-preview">
      <h4>Vuex store dump:</h4>
      <table>
      </table>
    </div>
  </div>
</template>

<script>
import { HotTable } from "@handsontable/vue";
import Handsontable from "handsontable";

export default {
  data() {
    return {
      hotSettings: {
        data: Handsontable.helper.createSpreadsheetData(4, 4),
        colHeaders: true,
        rowHeaders: true,
        readOnly: false,
        afterChange: () => {
          if (this.hotRef) {
            this.$store.commit("updateData", this.hotRef.getSourceData());
          }
        }
      },
      hotRef: null
    };
  },
  mounted: function() {
    this.hotRef = this.$refs.wrapper.hotInstance;
    this.$store.commit("updateData", this.hotRef.getSourceData());
  },
  components: {
    HotTable
  }
};
</script>

<style>
</style>
