<template>
  <div>
    <b-modal
      id="modal-3"
      size="lg"
      title="MRP New Data Configuration"
      no-stacking
    >
      <div class="row">
        <div class="col-4">
          <b-form-group label="File Type" class="border p-2">
            <b-form-radio v-model="rbSelected" name="file-type" value="Bill of Material"
              >Bill of Material</b-form-radio
            >
            <b-form-radio v-model="rbSelected" name="file-type" value="Master Schedule"
              >Master Schedule</b-form-radio
            >
            <b-form-radio v-model="rbSelected" name="file-type" value="Inventory Status"
              >Inventory Status</b-form-radio
            >
            <b-form-radio v-model="rbSelected" name="file-type" value="Item Master"
              >Item Master</b-form-radio
            >
            <b-form-radio v-model="rbSelected" name="file-type" value="Resource Capacity"
              >Resource Capacity</b-form-radio
            >
          </b-form-group>
        </div>
        <div class="col-8">
          <b-form-group class="border p-2 mt-3">
            <b-form-checkbox
              id="checkbox-1"
              v-model="status"
              name="checkbox-1"
              :value="true"
              :unchecked-value="false"
            >
              Create from BOM file: {{ rbSelected }}
            </b-form-checkbox>
          </b-form-group>
        </div>
      </div>
  
      <template v-slot:modal-footer="{ ok, cancel }">
        <b-button variant="secondary" @click="cancel()">
          Cancel
        </b-button>
        <b-button v-b-modal.modal-multi-2 variant="primary">
          OK
        </b-button>
      </template>
    </b-modal>

    <ModelParametersModal :tipo="rbSelected"/>
  </div>
</template>

<script>
import ModelParametersModal from "./ModelParametersModal"
export default {
  components: { ModelParametersModal },
  data() {
    return {
      status: Boolean,
      rbSelected: ""
    }
  }
};
</script>

<style></style>
