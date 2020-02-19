<template>
	<div>
		<b-modal id="file-store" title="Browse File" hide-footer>
			<p class="mb-2">Select BOM File:</p>
			<b-list-group class="overflow-auto mh-300">
				<b-list-group-item button v-for="file in allBomFiles" @click="ReturnSelected(file)" :key="file.id">{{ file.title }}</b-list-group-item>
			</b-list-group>
		</b-modal>
	</div>
</template>

<script>
import { mapActions, mapGetters, mapMutations } from "vuex";
export default {
	name: "fileListModal",
	methods: {
		...mapActions(["fetchBomFiles", "fetchItems"]),
		...mapMutations(["setBomFile"]),
		ReturnSelected(file) {
			this.setBomFile(file);
			this.fetchItems(file.id);
			this.$bvModal.hide("file-store");
			this.$emit("bomFile");
		}
	},
	mounted() {
		this.fetchBomFiles();
	},
	computed: {
		...mapGetters(["allBomFiles"])
	}
};
</script>

<style scoped>
.mh-300 {
	max-height: 300px;
}
</style>