<template>
  <div>
    <b-navbar type="dark" variant="dark" class="shadow-sm">
      <b-navbar-brand href="#" @click="goHome">STORM 5.0</b-navbar-brand>
    </b-navbar>
    <b-nav class="bg-white border">
        <b-dropdown id="dropdown-left" text="File" variant="white" class="m-2">
            <ModuleListModal/>
            <b-dropdown-item href="#">New Window</b-dropdown-item>
            <b-dropdown-item href="#">Open...</b-dropdown-item>
        </b-dropdown>

        <b-dropdown id="dropdown-right" right text="Edit" variant="white" class="m-2">
            <b-dropdown-item href="#">Copy</b-dropdown-item>
            <b-dropdown-item href="#">Paste</b-dropdown-item>
        </b-dropdown>
    </b-nav>
  </div>
</template>

<script>
import ModuleListModal from "./modals/ModuleListModal"
export default {
    components: { ModuleListModal },
    methods: {
      goHome() {
        this.$router.push('/')
      }
    }
};
</script>

<style>
.bg-second{
    background-color: #5e646b;
    color: white !important;
}
</style>