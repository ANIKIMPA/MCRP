<template>
	<div id="app">
		<Navbar v-if="$route.name != 'login' && $route.name != 'register'"/>
		<router-view :key="$route.fullPath" />

    <!-- Saved Toast -->
    <b-toast ref="toast" id="saved-toast" variant="success" solid toaster="b-toaster-bottom-right">
      <template v-slot:toast-title>
        <div class="d-flex flex-grow-1 align-items-baseline">
          <strong class="mr-auto">Storm 5.0</strong>
        </div>
      </template>
      Saved successfully!
    </b-toast>
	</div>
</template>

<script>
import Navbar from "@/components/Navbar";
import { mapGetters } from "vuex"

export default {
  components: { Navbar },
  computed: {
    ...mapGetters(["getError", "getInfo"])
  },
  watch: {
    getError() {
      this.$bvToast.toast(this.getError, {
        title: 'OOPS! Something went wrong',
        toaster: "b-toaster-bottom-right",
        variant: "danger",
        solid: true,
        autoHideDelay: 5000,
      })
    },
    getInfo() {
      console.log(this.$refs.toast.$slots.default[0].text = this.getInfo)
      this.$bvToast.show("saved-toast");
    }
  }
};
</script>

<style>
@import "./assets/styles/account.css";
#app {
	font-family: "Avenir", Helvetica, Arial, sans-serif;
	-webkit-font-smoothing: antialiased;
	-moz-osx-font-smoothing: grayscale;
	text-align: center;
}

.w-10 {
    width: 10%;
}

.modal-dialog {
	margin-top: 60px !important;
}

.handsontableEditor.autocompleteEditor.listbox.handsontable div.ht_master.handsontable div.wtHolder {
  height: 300px !important;
}

.handsontableEditor.autocompleteEditor.handsontable.listbox {
	height: 100% !important;
}

.handsontable.listbox td.htDimmed {
  background-color: #eceff1;
  padding: 8px;
  box-shadow: 10px;
}
.handsontable.listbox td.htDimmed:hover {
  /* background-color: #5292F7; */
  background-color: #bbdefb;
}

.handsontable.listbox tr td.current, .handsontable.listbox tr:hover td {
    background: #babdbe
}
</style>
