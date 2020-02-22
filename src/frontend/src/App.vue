<template>
	<div id="app">
		<Navbar />
		<router-view :key="$route.fullPath" />

    <b-toast id="error-toast" variant="danger" solid>
      <template v-slot:toast-title>
        <div class="d-flex flex-grow-1 align-items-baseline">
          <strong class="mr-auto">OOPS! Something went wrong</strong>
        </div>
      </template>
      {{ getError }}
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
</style>
