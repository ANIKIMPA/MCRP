<template>
	<div>
		<b-modal id="save-report" title="Report Title" hide-footer>

			<b-form @submit.prevent="onSubmit">
				<p v-if="form.error" class="errornote">{{ form.error }}</p>
				<b-form-group label-for="title">
					<b-form-input id="title" v-model="form.title" type="text" required placeholder="Enter a title for this report"></b-form-input>
				</b-form-group>

				<div class="text-right">
					<b-button type="submit" variant="primary">Save Report</b-button>
				</div>
			</b-form>
		</b-modal>
	</div>
</template>

<script>
import { mapActions, mapGetters, mapMutations } from "vuex";
export default {
	name: "SaveReportModal",
	data() {
		return {
			form: {
				title: "",
				error: ""
			}
		}
	},
	computed: {
		...mapGetters(["report"])
	},
	methods: {
		...mapActions(["createNewReport"]),
		...mapMutations(["setReportTitle"]),
		onSubmit() {
			if(this.form.title.trim() === "") {
				this.form.error = "The title cannot be empty."
			} else {
				if(isNaN(this.report.id) || this.report.id <= 0) {
					this.setReportTitle(this.form.title);
					this.createNewReport(this.report).then(() => {
						this.$bvToast.show("saved-toast");
						this.$router.push({
							name: "final_report",
							params: {
								report: this.report.id
							}
						});
					});
				}
			}

			this.$bvModal.hide("save-report");
		}
	}
};
</script>

<style>
</style>