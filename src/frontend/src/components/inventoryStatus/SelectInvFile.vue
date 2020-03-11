<template>
	<div>
		<b-button variant="outline-secondary" @click="openModal">Browse...</b-button>
		<b-modal id="inv-file-store" v-model="modalOpenned" title="Browse File" hide-footer>
			<p class="mb-2">Select INV File:</p>
			<b-list-group class="overflow-auto mh-300">
				<b-list-group-item button v-for="file in allInvFiles" @click="ReturnSelected(file)" :key="file.id" class="d-flex justify-content-between">
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
	name: "SelectInvFile",
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
		...mapActions(["fetchAllInvFiles", "fetchInvItems"]),
		...mapMutations(["setInvFile"]),
		ReturnSelected(file) {
			this.setInvFile(file);
			this.fetchInvItems(file.id);
			this.$bvModal.hide("inv-file-store");
		},
		openModal() {
			this.modalOpenned = true
			this.fetchAllInvFiles();
		}
	},
	computed: {
		...mapGetters(["allInvFiles"])
	}
};
</script>

<style scoped>
.mh-300 {
	max-height: 300px;
}
</style>