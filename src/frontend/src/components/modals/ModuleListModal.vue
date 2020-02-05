<template>
  <div>
    <b-dropdown-item v-b-modal.modal-1 href="#">New</b-dropdown-item>

    <!-- List Module Modal -->
    <b-modal id="modal-1" title="Module List" ok-only no-stacking>
        <p class="mb-2">Select module for new data:</p>
        <b-list-group class="overflow-auto mh-300">
          <b-list-group-item button @dblclick="DataConfigurationModal = true">Material Requirement Planning</b-list-group-item>
        </b-list-group>
    </b-modal>

    <!-- Data Configuration Modal -->
    <b-modal size="lg" v-model="DataConfigurationModal" title="MRP New Data Configuration" no-stacking>
      <div class="row">
        <div class="col-4">
          <b-form-group label="File Type" class="border p-2">
            <b-form-radio v-model="rbSelected" name="file-type" value="bm">Bill of Material</b-form-radio>
            <b-form-radio v-model="rbSelected" name="file-type" value="ms">Master Schedule</b-form-radio>
            <b-form-radio v-model="rbSelected" name="file-type" value="is">Inventory Status</b-form-radio>
            <b-form-radio v-model="rbSelected" name="file-type" value="im">Item Master</b-form-radio>
            <b-form-radio v-model="rbSelected" name="file-type" value="rc">Resource Capacity</b-form-radio>
          </b-form-group>
        </div>
        <div class="col-8">
          <b-form-group class="border p-2 mt-3">
            <b-form-checkbox id="checkbox-1" v-model="status" name="checkbox-1" :value="true" :unchecked-value="false">
              Create from BOM file: 
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

    <!-- MRP (BOM): Model Parameters -->
    <b-modal size="lg" id="modal-multi-2" title="MRP New Data Configuration" @ok="GoHome">
      <div class="form-group row">
        <label class="col-form-label col-2" for="title">Title:</label>
        <div class="col-10">
          <input type="text" class="form-control" v-model="title" name="title" id="title">
        </div>
      </div>
      <div class="form-group row">
        <label class="col-form-label col-9" for="items_number">Total Number of Items in the File</label>
        <div class="col-3">
          <input type="number" class="form-control" v-model="items_number" min="1" value="1" name="items_number" id="items_number">
        </div>
      </div>
      <div class="form-group row">
        <label class="col-form-label col-9" for="max_descendants">Maximal # of Immediate Descendants of any item:</label>
        <div class="col-3">
          <input type="number" class="form-control" min="0" value="0" v-model="max_descendants" name="max_descendants" id="max_descendants">
        </div>
      </div>
    </b-modal>
  </div>
</template>

<script>
export default {
  data() {
    return {
      status: Boolean,
      rbSelected: "",
      title: "",
      items_number: 1,
      max_descendants: 0,
      options: [
        "MRPDataConfigurationModal"
      ],
      DataConfigurationModal: false
    };
  },
  methods: {
    GoHome() {
      this.$router.push({name: 'home', params: {title: this.title,items_number: this.items_number,max_descendants: this.max_descendants}})
    }
  }
};
</script>

<style>
.mh-300 {
  max-height: 300px;
}
</style>