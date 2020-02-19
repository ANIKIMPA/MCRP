<template>
	<div>
        <li @click="openModal">BOM Files</li>
		<b-modal id="bom-file-list" v-model="modalOpenned" title="Bill of Material Files" hide-footer>
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
	name: "BomfileList",
	data() {
		return {
			modalOpenned: false
		}
	},
	methods: {
		...mapActions(["fetchAllBomFiles", "fetchItems"]),
		...mapMutations(["setBomFile"]),
		ReturnSelected(file) {
			this.setBomFile(file);
			this.fetchItems(file.id);
			this.$bvModal.hide("file-store");
			this.$emit("bomFile");
		},
		openModal() {
			this.modalOpenned = true
			this.fetchAllBomFiles();
		}
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