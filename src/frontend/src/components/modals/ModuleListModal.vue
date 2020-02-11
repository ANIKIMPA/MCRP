<template>
  <div>
    <b-dropdown-item v-b-modal.modal-1 href="#">New</b-dropdown-item>

    <!-- List Module Modal -->
    <b-modal id="modal-1" title="Module List" ok-only no-stacking>
      <p class="mb-2">Select module for new data:</p>
      <b-list-group class="overflow-auto mh-300">
        <b-list-group-item button v-b-modal.modal-3
          >Material Requirement Planning</b-list-group-item
        >
      </b-list-group>
    </b-modal>

    <DataConfigurationModal/>
  </div>
</template>

<script>

import DataConfigurationModal from "./DataConfigurationModal"
export default {
  components: { DataConfigurationModal },
};
</script>

<style>
.mh-300 {
  max-height: 300px;
}
</style>
