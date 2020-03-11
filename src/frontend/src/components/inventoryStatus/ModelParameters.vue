<template>
	<b-modal size="lg" id="modal-parameters" title="MRP (INV): Model Parameters" @ok.prevent="onSubmit">
		<form>
			<div class="form-group row">
				<label class="col-form-label col-2" for="title">Title:</label>
				<div class="col-10">
					<input type="text" class="form-control" v-model="form.title" id="title"/>
				</div>
			</div>

			<div class="form-group row">
				<!-- Numero de Items padres terminados -->
				<label class="col-form-label col-9" for="number_of_items">Total Number of Material Items:</label>
				<div class="col-3">
					<input type="number" class="form-control" min="1" v-model="form.number_of_items" :readonly="createFromBomFile" id="number_of_items" />
				</div>
			</div>
			<div class="form-group row">
				<label class="col-form-label col-9" for="number_of_periods">Maximal # of Periods for Firm Planned Orders:</label>
				<div class="col-3">
					<input type="number" class="form-control" v-model="form.number_of_periods" min="1" value="1" id="number_of_periods" readonly />
				</div>
			</div>
		</form>
	</b-modal>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
export default {
	name: "invModelParameters",
	props: {
		createFromBomFile: Boolean
	},
	data() {
		return {
			form: {
				title: "Inventory Status",
				number_of_periods: 1,
                number_of_items : 1,
			}
		};
	},
	computed: {
		...mapGetters(["invFile", "getAllBomItems"])
	},
	mounted() {
		this.$root.$on('bv::modal::show', (bvEvent, modalId) => {
			if(modalId === "modal-parameters")
				if(this.createFromBomFile) {
					this.form.title = this.getAllBomItems[0].part_number;
					this.form.number_of_items = this.getAllBomItems.length;
				} else {
					this.form.title = null
					this.form.number_of_items = 1
				}
		})

		const unsubscribe = this.$store.subscribe(mutation => {
			if (mutation.type === "newInvFile") {
				// Add items to the file
				this.addInvItems({
					items_number: this.form.number_of_items,
					part_numbers: this.getAllBomItems.map(item => this.createFromBomFile ? item.part_number : "-"),
					receipts: "0",
					file: this.invFile.id
				});
			}

			if (mutation.type === "setInvItems") {
				// Redirect to home page
				this.$router.push({
					name: "inventory_status",
					params: {
						file: this.invFile.id
					}
				});

				unsubscribe();
			}
		});

	},
	methods: {
		...mapActions(["addInvItems", "createNewInvFile"]),
		onSubmit() {
			if(this.form.title && this.form.title.trim() != "") {
				this.createNewInvFile({
					title: this.form.title,
					number_of_items: this.form.number_of_items,
                    number_of_periods: this.form.number_of_periods,
				});

				this.$nextTick(() => {
					this.$bvModal.hide('modal-parameters')
				})
			}
		}
	}
};
</script>

<style></style>