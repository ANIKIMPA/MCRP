<template>
	<div>
		<b-modal id="file-store" title="Browse File" hide-footer>
			<p class="mb-2">Select BOM File:</p>
			<b-list-group class="overflow-auto mh-300">
				<b-list-group-item button v-for="file in allFiles" @click="ReturnSelected(file)" :key="file.id">{{ file.title }}</b-list-group-item>
			</b-list-group>
		</b-modal>
	</div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
export default {
	name: "fileListModal",
	methods: {
		...mapActions(["fetchFiles"]),
		ReturnSelected(file) {
			this.$store.commit("setFile", file);
			this.$bvModal.hide("file-store");
			this.$emit("fileSelected");
		}
	},
	created() {
		this.fetchFiles();
	},
	computed: mapGetters(["allFiles"])
};
</script>

<style scoped>
.mh-300 {
	max-height: 300px;
}
</style>