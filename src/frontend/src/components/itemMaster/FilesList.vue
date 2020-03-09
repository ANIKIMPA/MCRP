<template>
	<div>
		<li @click="openModal">ITEM Files</li>
		<b-modal id="item-master-file-list" v-model="modalOpenned" title="Item Master Files" hide-footer>
			<p class="mb-2">Select ITEM File:</p>
			<b-list-group class="overflow-auto mh-300">
				<b-list-group-item button v-for="file in allItemMasterFiles" @click="openItemMaster(file)" :key="file.id" class="d-flex justify-content-between">
					<span style="width: 50%"><i class="fas fa-file-alt"></i> {{ file.title }}</span>
					<small style="font-style: italic;">{{ file.created_date | formatDate }}</small>
					<a href="#" @click.stop.prevent="deleteFile(file)" class="text-danger px-1" style="text-align:right;"><i class="fas fa-trash-alt"></i></a>
				</b-list-group-item>
			</b-list-group>
		</b-modal>
	</div>
</template>

<script>
import moment from "moment";
import { mapActions, mapGetters, mapMutations } from "vuex";
export default {
	name: "ItemMasterFilesList",
	data() {
		return {
			modalOpenned: false
		};
	},
	filters: {
		formatDate(value) {
			return moment(value).format("L") + " " + moment(value).format("hh:mma");
		}
	},
	methods: {
		...mapActions(["fetchAllItemMasterFiles", "deleteItemMasterFile"]),
		...mapMutations(["setItemMasterFile"]),
		openItemMaster(file) {
			this.$router.push({
				name: "item_master",
				params: {
					file: file.id
				}
			});
			this.setItemMasterFile(file);
			this.$bvModal.hide("item-master-file-list");
		},
		openModal() {
			this.modalOpenned = true;
			this.fetchAllItemMasterFiles();
		},
    deleteFile(file) {
      if (this.itemMasterFile.id === file.id) {
        this.$router.push("/");
      }
      file.removed = true
			this.deleteItemMasterFile(file);
		}
	},
	computed: {
		...mapGetters(["allItemMasterFiles", "itemMasterFile"])
	}
};
</script>

<style>
.mh-300 {
	max-height: 300px;
}
</style>