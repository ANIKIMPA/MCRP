<template>
	<div class="row justify-content-between no-gutters" v-if="isValidData">

		<table class="col-lg-5half mb-4" v-for="(bomItem, idx) in getAllBomItems" :key="idx">
			<tr>
				<td width="22%" class="border-dark bg-azulito">Item Number</td>
				<td width="22%" class="border-dark">{{ bomItem.part_number }}</td>
				<td width="12%" class="border-dark empty-cell">&nbsp;</td>
				<td width="22%" class="border-dark bg-azulito">Yield (%)</td>
				<td width="22%" class="border-dark">{{ getAllItemsMasters[idx].yield_percent | percentage }}</td>
			</tr>
			<tr>
				<td class="border-dark bg-azulito">Lead Time</td>
				<td class="border-dark">{{ getAllItemsMasters[idx].lead_time }}</td>
				<td class="border-dark empty-cell">&nbsp;</td>
				<td class="border-dark bg-azulito">Order Cost</td>
				<td class="border-dark">{{ getAllItemsMasters[idx].order_cost | dollarFormat }}</td>
			</tr>
			<tr>
				<td class="border-dark bg-azulito">Parent</td>
				<td class="border-dark">{{ bomItem.parent }}</td>
				<td class="border-dark empty-cell">&nbsp;</td>
				<td class="border-dark bg-azulito">Carrying Cost</td>
				<td class="border-dark">{{ getAllItemsMasters[idx].carrying_cost | dollarFormat }}</td>
			</tr>
			<tr>
				<td class="border-dark bg-azulito">Quantity</td>
				<td class="border-dark">{{ bomItem.qty }}</td>
				<td class="border-dark empty-cell">&nbsp;</td>
				<td class="border-dark bg-azulito">Lot Size</td>
				<td class="border-dark">{{ getAllItemsMasters[idx].lot_size }}</td>
			</tr>
			<tr>
				<td class="border-dark bg-azulito">Safety Stock</td>
				<td class="border-dark">{{ getAllInvItems[idx].safe_stock }}</td>
				<td class="border-dark empty-cell">&nbsp;</td>
				<td class="border-dark bg-azulito">Factor</td>
				<td class="border-dark">&nbsp;</td>
			</tr>
			<tr>
				<td class="border-dark empty-cell">&nbsp;</td>
				<td class="border-dark empty-cell">&nbsp;</td>
				<td class="border-dark empty-cell">&nbsp;</td>
				<td class="border-dark bg-azulito">On hand</td>
				<td class="border-dark empty-cell">&nbsp;</td>
			</tr>
			<tr>
				<td class="border-dark bg-azulito">Period</td>
				<td class="border-dark bg-azulito">Gross Requirement</td>
				<td class="border-dark bg-azulito">Receipts</td>
				<td class="border-dark">{{ getAllInvItems[idx].on_hand }}</td>
				<td class="border-dark bg-azulito">Net Requirement</td>
			</tr>
			<tr v-for="(period, i) in periods(idx)" :key="i">
				<td class="border-dark">{{ i + 1 }}</td>
				<td class="border-dark">{{ period }}</td>
				<td class="border-dark"></td>
				<td class="border-dark"></td>
				<td class="border-dark"></td>
			</tr>
		</table>
	</div>
</template>

<script>
import { mapGetters, mapMutations } from "vuex"

export default {
	name: "FinalReport",
	data() {
		return {
			isValidData: false
		}
	},
	computed: {
		...mapGetters(["getAllBomItems", "getAllInvItems", "getAllMastItems", "getAllItemsMasters"])
	},
	methods: {
		...mapMutations(["throwError"]),
		periods: function(idx) {
			if(idx < this.getAllMastItems.length) {
				return this.getAllMastItems[idx].periods.split(",");
			} else {
				return ["", "", "", "", "", "", "", "", "", ""];
			}
		},
		dataFilesMatch() {
			if(this.getAllBomItems.length <= 0 || this.getAllInvItems.length <= 0 ||
				this.getAllItemsMasters.length <= 0 || this.getAllMastItems.length <= 0) {
				this.$router.push({
					name: "home"
				})
				return false
			}

			const bomItems = this.getAllBomItems.map((item) => item.part_number)
			const invItems = this.getAllInvItems.map((item) => item.part_number)
			const itemsMasters = this.getAllItemsMasters.map((item) => item.part_number)

			// Validate part numbers in Master Schedule file match.
			this.getAllMastItems.map((item) => item.part_number).forEach((part_number) => {
				if(!bomItems.includes(part_number)) {
					this.throwError(`The part number: ${part_number} doesn't match in Master Schedule.`)
					this.$router.push({
						name: "home"
					})
					return false
				}
			})

			// Validate part numbers in inventory status file
			// and item master files matches.
			for(let idx=0; idx<bomItems.length; idx++) {
				if(bomItems[idx] !== invItems[idx]) {
					this.throwError(`The part number: ${invItems[idx]} doesn't match in Inventory Status.`)
					this.$router.push({
						name: "home"
					})
					return false
				} else if(bomItems[idx] !== itemsMasters[idx]) {
					this.throwError(`The part number: ${itemsMasters[idx]} doesn't match in Item Master.`)
					this.$router.push({
						name: "home"
					})
					return false
				}
			}

			return true
		}
	},
	filters: {
		percentage(value) {
			return parseFloat(value * 100).toFixed(1) + "%";
		},
		dollarFormat(value) {
			return "$" + parseFloat(value).toFixed(2);
		}
	},
	mounted() {
		this.isValidData = this.dataFilesMatch()
	}
};
</script>

<style>
.border-dark {
	background-color: #f9ffff;
	border: #000000 solid 1px;
}
.bg-azulito {
	background-color: #d3f7fd;
}
.empty-cell:first-child {
	border-left: #000000 solid 1px;
}
.empty-cell:last-child {
	border-right: #000000 solid 1px;
}
tr:first-child .empty-cell:nth-last-child(3) {
	border-top: #000000 solid 1px;
}
.empty-cell {
	border: 0;
	background-color: #e1e7e7;
}

.col-lg-5half {
	position: relative;
	min-height: 1px;
	padding-right: 15px;
	padding-left: 15px;
	width: 100%;
}

@media (min-width: 960px) {
	.col-lg-5half {
		float: left;
	}
	.col-lg-5half {
		width: 49%;
	}
}
</style>