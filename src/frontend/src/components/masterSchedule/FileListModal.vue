<template>
	<div>
		<b-button :disabled="!createFromBomFile" variant="outline-secondary" @click="openModal">Browse...</b-button>
		<b-modal id="file-store" v-model="modalOpenned" title="Browse File" hide-footer>
			<p class="mb-2">Select BOM File:</p>
			<b-list-group class="overflow-auto mh-300">
				<b-list-group-item button v-for="file in allBomFiles" @click="ReturnSelected(file)" :key="file.id" class="d-flex justify-content-between">
					<span><i class="far fa-file-alt"></i> {{ file.title }}</span> <small style="font-style: italic;">{{ file.created_date | formatDate }}</small>
				</b-list-group-item>
			</b-list-group>
		</b-modal>
	</div>
</template>

<script>
import { mapActions, mapGetters, mapMutations } from "vuex";
import moment from "moment";
export default {
	name: "fileListModal",
	props: {
		createFromBomFile: Boolean
	},
	data() {
		return {
			modalOpenned: false
		}
	},
	filters: {
		formatDate(value) {
			return moment(value).format("L") + " " + moment(value).format("hh:mma");
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