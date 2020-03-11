<template>
	<b-modal size="lg" id="modal-parameters" title="MRP (ITEM): Model Parameters" @ok.prevent="onSubmit">
		<form>
			<div class="form-group row">
				<label class="col-form-label col-2" for="title">Title:</label>
				<div class="col-10">
					<input type="text" class="form-control" v-model="form.title" id="title" />
				</div>
			</div>

			<div class="form-group row">
				<!-- Numero de Items padres terminados -->
				<label class="col-form-label col-9" for="number_of_items">Total Number of Material Items:</label>
				<div class="col-3">
					<input type="number" class="form-control" min="1" v-model="form.number_of_items" :readonly="createFromBomFile" id="number_of_items" />
				</div>
			</div>
		</form>
	</b-modal>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
export default {
	name: "itemMasterModelParameters",
	props: {
		createFromBomFile: Boolean
	},
	data() {
		return {
			form: {
				title: "",
				number_of_items: 1,
				number_of_periods: 1
			}
		};
	},
	computed: {
		...mapGetters(["itemMasterFile", "getAllBomItems"])
	},
	mounted() {
		this.$root.$on("bv::modal::show", (bvEvent, modalId) => {
			if (modalId === "modal-parameters")
				if (this.createFromBomFile) {
					this.form.title = this.getAllBomItems[0].part_number;
					this.form.number_of_items = this.getAllBomItems.length;
				} else {
					this.form.title = null;
					this.form.number_of_items = 1;
				}
		});

		const unsubscribe = this.$store.subscribe(mutation => {
			if (mutation.type === "newItemMasterFile") {
				// Add items to the file
				this.addItemsMasters({
					items_number: this.form.number_of_items,
					part_numbers: this.getAllBomItems.map(item => this.createFromBomFile ? item.part_number : "-"),
					file: this.itemMasterFile.id
				});
			}

			if (this.mutation === "setItemsMasters") {
				// Redirect to home page
				this.$router.push({
					name: "item_master",
					params: {
						file: this.itemMasterFile.id
					}
				});

				unsubscribe();
			}
		});
	},
	methods: {
		...mapActions(["addItemsMasters", "createNewItemMasterFile"]),
		onSubmit() {
			if (this.form.title && this.form.title.trim() != "") {
				this.createNewItemMasterFile({
					title: this.form.title,
					number_of_items: this.form.number_of_items
				});

				this.$nextTick(() => {
					this.$bvModal.hide("modal-parameters");
				});
			}
		}
	}
};
</script>

<style></style>