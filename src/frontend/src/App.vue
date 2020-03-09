<template>
	<div id="app">
		<Navbar />
		<router-view :key="$route.fullPath" />

    <!-- Error Toast -->
    <b-toast id="error-toast" variant="danger" solid>
      <template v-slot:toast-title>
        <div class="d-flex flex-grow-1 align-items-baseline">
          <strong class="mr-auto">OOPS! Something went wrong</strong>
        </div>
      </template>
      {{ getError }}
    </b-toast>

    <!-- Saved Toast -->
    <b-toast id="saved-toast" variant="success" solid>
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
    ...mapGetters(["getError"])
  },
	mounted() {
		this.$store.subscribe(mutation => {
			if (mutation.type === "throwError") {
				this.$bvToast.show("error-toast");
			}
		});
	}
};
</script>

<style>
#app {
	font-family: "Avenir", Helvetica, Arial, sans-serif;
	-webkit-font-smoothing: antialiased;
	-moz-osx-font-smoothing: grayscale;
	text-align: center;
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
