<template>
  <div>
      <i style="color: #a9a9a9">Row: {{row}}, column: {{col}},</i> value: {{value}}
  </div>
</template>

<script>
export default {
    data() {
        // Define properties in our data object,
        // corresponding to all of the data being injected from
        // the BaseEditorComponent class, which are:
        // - hotInstance (instance of Handsontable)
        // - row (row index)
        // - col (column index)
        // - prop (column property name)
        // - TD (the HTML cell element)
        // - cellProperties (the cellProperties object for the edited cell)
        return {
            hotInstance: null,
            TD: null,
            row: null,
            col: null,
            prop: null,
            value: null,
            cellProperties: null
        }
    }
}
</script>

<style>

</style>