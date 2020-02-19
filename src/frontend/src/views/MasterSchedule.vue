<template>
	<div>
		<hot-table ref="hotTableComponent" :settings="settings"></hot-table>

		<b-toast id="my-toast" variant="success" solid>
			<template v-slot:toast-title>
				<div class="d-flex flex-grow-1 align-items-baseline">
					<strong class="mr-auto">Storm 5.0</strong>
				</div>
			</template>
			Saved successfully!
		</b-toast>
	</div>
</template>

<script>
import { HotTable } from "@handsontable/vue";
import { mapGetters, mapActions } from "vuex";
// import Handsontable from 'handsontable';

export default {
	name: "master_schedule",
	components: {
		HotTable
		// HotColumn
	},
	data() {
		return {
			hotRef: null,
			settings: {
				data: [],
				colHeaders: ["Part Number"],
				stretchH: "all",
				colWidths: 100,
				afterChange: changes => {
					if (changes) {
						changes.forEach(([row]) => {
							try {
								this.updateMasterSchedule(this.settings.data[row]);
								this.$bvToast.show("my-toast");
							} catch (error) {
								console(error);
							}
						});
					}
				},
				columns: [],
				rowHeights: 40,
				rowHeaders: true,
				licenseKey: "non-commercial-and-evaluation",
				className: "htMiddle htCenter"
			}
		};
	},
	computed: {
		...mapGetters(["getAllPeriods", "mastFile"])
	},
	created() {
		this.fetchMastFile(this.$route.params.file);
		this.fetchPeriods(this.$route.params.file);


		this.$store.subscribe(mutation => {
			if (mutation.type === "setMastFile") {
				console.log(this.mastFile.planning_horizon_length);
				this.settings.columns.push({
					data: "part_number",
					allowEmpty: false
				});
				for (let i = 1; i <= this.mastFile.planning_horizon_length * 1; i++) {
					this.settings.colHeaders.push("Period " + i);
					this.settings.columns.push({
						data: "period" + i,
						allowEmpty: false
					});
				}

				this.hotRef = this.$refs.hotTableComponent.hotInstance;
				this.$store.commit("updatePeriods", this.hotRef.getSourceData());
			}
		});
	},
	mounted: function() {
		// this.hotRef = this.$refs.hotTableComponent.hotInstance;
		// this.$store.commit("updatePeriods", this.hotRef.getSourceData());
	},
	methods: {
		...mapActions(["fetchMastFile", "fetchPeriods"])
	}
};
</script>

<style>
@import "~handsontable/dist/handsontable.full.css";
</style>