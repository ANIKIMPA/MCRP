<template>
	<b-modal size="lg" id="modal-multi-2" title="MRP (MAST): Model Parameters" @ok="onSubmit">
		<form>
			<div class="form-group row">
				<label class="col-form-label col-2" for="title">Title:</label>
				<div class="col-10">
					<input type="text" class="form-control" v-model="form.title" id="title" />
				</div>
			</div>

			<div class="form-group row">
				<!-- Numero de Items padres terminados -->
				<label class="col-form-label col-9" for="master_items">Number of Items Master Scheduled:</label>
				<div class="col-3">
					<input type="number" class="form-control" min="1" :value="this.getMasterItems.length" readonly id="master_items" />
				</div>
			</div>
			<div class="form-group row">
				<!-- Número de periodos -->
				<label class="col-form-label col-9" for="planning_horizon_length">Planning Horizon Length in Time Buckets:</label>
				<div class="col-3">
					<input type="number" class="form-control" v-model="form.planning_horizon_length" min="1" value="1" id="planning_horizon_length" />
				</div>
			</div>
			<div class="form-group row">
				<label class="col-form-label col-9" for="number_time_buckets">Number of Time Buckets per Year:</label>
				<div class="col-3">
					<input type="number" class="form-control" v-model="form.number_time_buckets" min="1" value="1" id="number_time_buckets" />
				</div>
			</div>
		</form>
	</b-modal>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
export default {
	name: "mastModelParameters",
	data() {
		return {
			form: {
				title: "Master Scheduled",
				planning_horizon_length: 0,
				number_time_buckets: 0
			}
		};
	},
	computed: {
		...mapGetters(["mastFile", "getMasterItems"])
	},
	mounted() {
		this.$store.subscribe(mutation => {
			if (mutation.type === "newMastFile") {
				// Add items to the file
				for (let i = 0; i < this.getMasterItems.length; i++) {
					for (let num = 1; num <= this.form.planning_horizon_length; num++) {
						this.addPeriod({
							part_number: this.getMasterItems[i].part_number,
							period: null,
							order: num,
							file: this.mastFile.id
						});
					}
				}

				// Redirect to home page
				this.$router.push({
					name: "master_schedule",
					params: {
						file: this.mastFile.id
					}
				});
			}
		});
	},
	methods: {
		...mapActions(["addPeriod", "createNewMastFile"]),
		onSubmit() {
			this.createNewMastFile({
				title: this.form.title,
				number_of_items: this.getMasterItems.length,
				planning_horizon_length: this.form.planning_horizon_length,
				number_time_buckets: this.form.number_time_buckets
			});
		}
	}
};
</script>

<style></style>
