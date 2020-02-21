<template>
	<b-modal size="lg" id="modal-parameters" title="MRP (BOM): Model Parameters" @ok="GoHome">
		<div class="form-group row">
			<label class="col-form-label col-2" for="title">Title:</label>
			<div class="col-10">
				<input type="text" class="form-control" v-model="title" id="title" />
			</div>
		</div>
		<div class="form-group row">
			<label class="col-form-label col-9" for="items_number">Total Number of Items in the File</label>
			<div class="col-3">
				<input type="number" class="form-control" v-model="items_number" min="1" value="1" id="items_number" />
			</div>
		</div>
	</b-modal>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
export default {
	name: "bomModelParameters",
	data() {
		return {
			title: "",
			items_number: 1
		};
	},
	computed: {
		...mapGetters(["bomFile"])
	},
	created() {
		this.$store.subscribe(mutation => {
			if (mutation.type === "newBomFile") {
				// Add items to the file
				for (let i = 1; i <= this.items_number; i++) {
					this.addItem({
						part_number: 100 * i,
						tipo: "MAT",
						parent: null,
						qty: 1,
						file: this.bomFile.id
					});
				}

				// Redirect to home page
				this.$router.push({
					name: "bill_of_material",
					params: {
						file: this.bomFile.id
					}
				});
			}
		});
	},
	methods: {
		...mapActions(["addItem", "createNewBomFile"]),
		GoHome() {
			// Create new file
			this.createNewBomFile({
				title: this.title,
				number_of_items: this.items_number
			});
		}
	}
};
</script>

<style></style>
