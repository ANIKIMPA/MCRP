<template>
  <div>
    <b-navbar type="dark" variant="dark" class="shadow-sm">
      <b-navbar-brand href="#" @click="goHome">STORM 5.0</b-navbar-brand>
    </b-navbar>
    <b-nav class="bg-white border">
      <b-dropdown id="dropdown-left" text="File" variant="white" class="m-2">
        <b-dropdown-item v-b-modal.modal-1 href="#">New</b-dropdown-item>
        <b-dropdown-item href="#">Open...</b-dropdown-item>
        <b-dropdown-item href="#" @click="goHome">Close</b-dropdown-item>
        <b-dropdown-item href="#">Close All</b-dropdown-item>
        <b-dropdown-item href="#">New Window</b-dropdown-item>
      </b-dropdown>

      <b-dropdown id="dropdown-right" right text="Edit" variant="white" class="m-2">
        <b-dropdown-item href="#">Copy</b-dropdown-item>
        <b-dropdown-item href="#">Paste</b-dropdown-item>
      </b-dropdown>
    </b-nav>

    <ModuleListModal />
    <DataConfigurationModal @fileSelected="saveFile" />
    <ModelParametersModal :tipo="fileTypeSelected" />
  </div>
</template>

<script>
import ModuleListModal from "./billOfMaterial/ModuleListModal";
import DataConfigurationModal from "./DataConfigurationModal";
import ModelParametersModal from "./billOfMaterial/ModelParametersModal";
export default {
  components: {
    ModuleListModal,
    DataConfigurationModal,
    ModelParametersModal
  },
  data() {
    return {
      createFromBomFile: false,
      fileTypeSelected: ""
    };
  },
  methods: {
    goHome() {
      this.$router.push("/");
    },
    saveFile(fileType) {
      this.fileTypeSelected = fileType
    }
  }
};
</script>

<style>
.bg-second {
  background-color: #5e646b;
  color: white !important;
}
</style>
