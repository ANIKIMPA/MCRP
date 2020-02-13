<template>
  <div>
    <b-modal id="data-config" size="lg" title="MRP New Data Configuration">
      <b-row>
        <b-col>
          <b-form-group label="File Type" class="h-92 border p-2">
            <b-form-radio
              v-model="fileTypeSelected"
              name="file-type"
              value="Bill of Material"
            >Bill of Material</b-form-radio>
            <b-form-radio
              v-model="fileTypeSelected"
              name="file-type"
              value="Master Schedule"
            >Master Schedule</b-form-radio>
            <b-form-radio
              v-model="fileTypeSelected"
              name="file-type"
              value="Inventory Status"
            >Inventory Status</b-form-radio>
            <b-form-radio
              v-model="fileTypeSelected"
              name="file-type"
              value="Item Master"
            >Item Master</b-form-radio>
            <b-form-radio
              v-model="fileTypeSelected"
              name="file-type"
              value="Resource Capacity"
            >Resource Capacity</b-form-radio>
          </b-form-group>
        </b-col>
        <b-col cols="8">
          <div v-if="fileTypeSelected != 'Bill of Material' && fileTypeSelected != ''" class="border p-2 my-3">
            <b-form-group>
              <b-row align-h="between" align-v="center">
                <b-col cols="6">
                  <b-form-checkbox
                    v-model="createFromBomFile"
                    :value="true"
                    :unchecked-value="false"
                  >Create from BOM file:</b-form-checkbox>
                </b-col>
                <b-col cols="4">
                  <b-button :disabled="!createFromBomFile" variant="outline-secondary" v-b-modal.file-store>Browse...</b-button>
                </b-col>
              </b-row>
            </b-form-group>
  
            <b-form-group>
              <b-form-input :disabled="!createFromBomFile" v-model="fileTitle" readonly></b-form-input>
            </b-form-group>
  
            <b-form-group label-cols-sm="6" :class="{ disabled: !createFromBomFile }" label="Copy Items:" label-align-sm="left" class="mb-0">
              <b-col cols="12">
                <b-form-radio-group :disabled="!createFromBomFile" :options="['Lowest Level', 'Selected']" />
              </b-col>
            </b-form-group>
          </div>
        </b-col>
      </b-row>

      <template v-slot:modal-footer="{ ok, cancel }">
        <b-button variant="secondary" @click="cancel()">Cancel</b-button>
        <b-button v-b-modal.modal-multi-2 variant="primary">OK</b-button>
      </template>
    </b-modal>

    <FileStore @fileSelected="getFileSelected"/>
    <ModelParameters />
  </div>
</template>

<script>
import FileStore from "./FileStore";
import ModelParameters from "./masterSchedule/ModelParameters";
export default {
  components: { FileStore, ModelParameters },
  data() {
    return {
      createFromBomFile: false,
      fileTypeSelected: "Bill of Material",
      fileTitle: ""
    }
  },
  watch: {
    fileTypeSelected: function() {
      if(this.fileTypeSelected.trim() != "") {
        this.$emit("fileSelected", this.fileTypeSelected)
      }
    }
  },
  mounted() {
    this.$emit("fileSelected", this.fileTypeSelected)
  },
  methods: {
    getFileSelected(file) {
      this.fileTitle = file.title
    }
  }
};
</script>

<style scoped>
.h-92 {
  height: 92%;
}
.disabled {
  color: #6c757d;
}
</style>
