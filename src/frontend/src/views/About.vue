<template>
  <div>
    <table class="border-dark m-auto">
      <tr>
        <td class="border">
          <label for="item_number">Item Number</label>
        </td>
        <td class="border">
          <input class="form-control" type="text" id="item_number">
        </td>
        <td class="border">&nbsp;</td>
        <td class="border">
          <label for="yield">Yield (%)</label>
        </td>
        <td class="border">
          <input class="form-control" type="text" id="yield">
        </td>
      </tr>
    </table>
  </div>
</template>

<script>
export default {
  
};
</script>

<style>
  .border-dark {
    border: #000000 solid 1px;
  }
</style>
