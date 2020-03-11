<template>
	<div>
		<label class="title">Item Master: {{ itemMasterFile.title }}</label>
		<hot-table :settings="settings"></hot-table>
	</div>
</template>

<script>
import store from "@/store";
import validator from "@/js/validator";
import { HotTable } from "@handsontable/vue";
import { mapGetters, mapActions } from "vuex";

export default {
	name: "ItemMaster",
	store,
	components: {
		HotTable
	},
	data() {
		return {
			settings: {
				data: [],
				colHeaders: [
					"Part Number",
					"Lot Size",
					"Multiple",
					"Lead Time",
					"Yield %",
					"Unit Value",
					"Order Cost",
					"Carrying Cost",
					"Demand"
				],
				stretchH: "all",
				colWidths: 50,
				afterChange: changes => {
					if (changes) {
						changes.forEach(([row]) => {
							this.updateItemMaster(this.settings.data[row]);
						});
					}
				},
				columns: [
					{
						data: "part_number",
						validator: (value, callback) => callback(validator.isNotEmpty(value)),
					},
					{
						data: "lot_size",
						type: "dropdown",
						source: ["LFL", "FP", "FQ", "EOQ"]
					},
					{
						data: "multiple",
						type: "numeric",
						validator: (value, callback) => callback(validator.isPositive(value)),
					},
					{
						data: "lead_time",
						type: "numeric",
						validator: (value, callback) => callback(validator.isPositive(value)),
					},
					{
						data: "yield_percent",
						validator: validator.isValidPercent,
						type: "numeric",
						numericFormat: {
							pattern: "0.0%",
							culture: "en-US"
						}
					},
					{
						data: "unit_value",
						validator: (value, callback) => callback(validator.isPositive(value)),
						type: "numeric",
						numericFormat: {
							pattern: "$0,0.00",
							culture: "en-US"
						}
					},
					{
						data: "order_cost",
						validator: (value, callback) => callback(validator.isPositive(value)),
						type: "numeric",
						numericFormat: {
							pattern: "$0,0.00",
							culture: "en-US"
						}
					},
					{
						data: "carrying_cost",
						validator: (value, callback) => callback(validator.isPositive(value)),
						type: "numeric",
						numericFormat: {
							pattern: "$0,0.00",
							culture: "en-US"
						}
					},
					{
						data: "demand",
						type: "numeric",
						validator: (value, callback) => callback(validator.isPositive(value)),
					}
				],
				beforeRemoveRow: (_, amount, physicalRows) => {
					physicalRows.forEach(index => {
						this.deleteItemMaster(this.settings.data[index]);
					});
				},
				rowHeights: 40,
				rowHeaders: true,
				licenseKey: "non-commercial-and-evaluation",
				className: "htMiddle htCenter",
				manualColumnResize: true,
				manualRowResize: true,
				contextMenu: {
					items: {
						add_row: {
							name: "Add item row",
							callback: this.addRow
						},
						remove_row: {
							disabled: validator.allRowsSelected
						},
						"---------": {},
						copy: {},
						cut: {}
					}
				}
			}
		};
	},
	computed: {
		...mapGetters([
			"getAllItemsMasters",
			"itemMasterFile"
		])
	},

	created() {
		this.fetchItemMasterFile(this.$route.params.file);

		this.$store.subscribe(mutation => {
			if (mutation.type === "setItemsMasters") {
				this.settings.data = this.getAllItemsMasters;
			}

			if (mutation.type === "updatedItemMaster" || mutation.type === "deletedItemMaster")
				this.$bvToast.show("saved-toast");
		});
	},
	mounted() {
		this.fetchItemsMasters(this.$route.params.file);
	},
	methods: {
		...mapActions([
			"fetchItemMasterFile",
			"fetchItemsMasters",
			"updateItemMaster",
			"addItemsMasters",
			"deleteItemMaster"
		]),
		addRow() {
			this.addItemsMasters({
				items_number: 1,
				part_numbers: "-",
				order: this.getAllItemsMasters.length,
				file: this.itemMasterFile.i
			});
			this.$bvToast.show("saved-toast");
		}
	}
};
</script>

<style scoped>
@import "~handsontable/dist/handsontable.full.css";

.title {
	position: absolute;
	top: 16px;
	color: #ffffff;
	z-index: 200;
	left: 50%;
	width: 600px;
	margin-left: -300px;
}
</style>