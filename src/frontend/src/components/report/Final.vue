<template>
	<div class="row justify-content-between no-gutters" v-if="isValidData">

		<table class="col-lg-5half mb-5 shadow" v-for="(item, idx) in data" :key="idx">
			<tr>
				<td width="20%" class="border-dark bg-azulito">Part Number</td>
				<td width="22%" class="border-dark">{{ item.part_number }}</td>
				<td width="18%" class="border-dark empty-cell">&nbsp;</td>
				<td width="20%" class="border-dark bg-azulito">Yield (%)</td>
				<td width="20%" class="border-dark">{{ item.yield_percent | percentage }}</td>
			</tr>
			<tr>
				<td class="border-dark bg-azulito">Lead Time</td>
				<td class="border-dark">{{ item.lead_time }}</td>
				<td class="border-dark empty-cell">&nbsp;</td>
				<td class="border-dark bg-azulito">Order Cost</td>
				<td class="border-dark">{{ item.order_cost | dollarFormat }}</td>
			</tr>
			<tr>
				<td class="border-dark bg-azulito">Parent</td>
				<td class="border-dark">{{ item.parent }}</td>
				<td class="border-dark empty-cell">&nbsp;</td>
				<td class="border-dark bg-azulito">Carrying Cost</td>
				<td class="border-dark">{{ item.carrying_cost | dollarFormat }}</td>
			</tr>
			<tr>
				<td class="border-dark bg-azulito">Quantity</td>
				<td class="border-dark">{{ item.qty }}</td>
				<td class="border-dark empty-cell">&nbsp;</td>
				<td class="border-dark bg-azulito">Lot Size</td>
				<td class="border-dark">{{ item.lot_size }}</td>
			</tr>
			<tr>
				<td class="border-dark bg-azulito">Safety Stock</td>
				<td class="border-dark">{{ item.safe_stock }}</td>
				<td class="border-dark empty-cell">&nbsp;</td>
				<td class="border-dark bg-azulito">Factor</td>
				<td class="border-dark">&nbsp;</td>
			</tr>
			<tr>
				<td class="border-dark empty-cell">&nbsp;</td>
				<td class="border-dark empty-cell">&nbsp;</td>
				<td class="border-dark empty-cell">&nbsp;</td>
				<td class="border-dark bg-azulito">On Hand</td>
				<td class="border-dark empty-cell">&nbsp;</td>
			</tr>
			<tr>
				<td class="border-dark bg-azulito">Period</td>
				<td class="border-dark bg-azulito">Gross Requirement</td>
				<td class="border-dark bg-azulito">Receipts</td>
				<td class="border-dark">{{ item.on_hand }}</td>
				<td class="border-dark bg-azulito">Net Requirement</td>
			</tr>
			<tr v-for="(period, i) in item.periods" :key="i">
				<td class="border-dark">{{ i + 1 }}</td>
				<td class="border-dark">{{ period.gross_requirement }}</td>
				<td class="border-dark">{{ period.receipt }}</td>
				<td class="border-dark">{{ period.on_hand }}</td>
				<td class="border-dark">{{ period.net_requirement }}</td>
			</tr>
			<tbody>
				<tr>
					<td colspan="5" class="border-dark empty-cell">&nbsp;</td>
				</tr>
				<tr>
					<th class="border-dark bg-azulito">Total Inventory</th>
					<th class="border-dark bg-azulito">Average Inventory</th>
					<th class="border-dark bg-azulito">Hauling Cost</th>
					<th class="border-dark bg-azulito">Order Cost</th>
					<th class="border-dark bg-azulito">Total Cost</th>
				</tr>
				<tr>
					<td class="border-dark">{{ item.totalInventory }}</td>
					<td class="border-dark">{{ item.averageInventory }}</td>
					<td class="border-dark">{{ item.haulingCost | dollarFormat }}</td>
					<td class="border-dark">{{ item.orderCost | dollarFormat }}</td>
					<td class="border-dark">{{ item.totalCost | dollarFormat }}</td>
				</tr>
			</tbody>
		</table>
	</div>
</template>

<script>
import { mapGetters, mapMutations, mapActions } from "vuex"

export default {
	name: "FinalReport",
	data() {
		return {
			isValidData: false,
			data: []
		}
	},
	computed: {
		...mapGetters(["getAllBomItems", "getAllInvItems", "getAllMastItems", "getAllItemsMasters", "report"])
	},
	methods: {
		...mapActions(["fetchReport"]),
		...mapMutations(["throwError", "setReportItems"]),
		periodsData: function(index) {
			let items = []

			// Obtain gross requirements regarding whether item has a parent or not.
			let gross_requirements = []
			if(this.getAllBomItems[index].parent) {
				gross_requirements = this.data.find((item) => item.part_number == this.getAllBomItems[index].parent).periods.map((period) => period.net_requirement * this.getAllBomItems[index].qty)
			} else {
				gross_requirements = this.getAllMastItems[index].periods.split(",").map((period) => period * this.getAllBomItems[index].qty);
			}

			let prev_receipts = this.getAllInvItems[index].receipts.split(",").map((receipt) => parseInt(receipt));
			let on_hands = [];
			let net_requirements = [];
			let receipts = [];

			// First receipts and on hands before lead time.
			for(let idx=0; idx<this.getAllItemsMasters[index].lead_time; idx++) {
				receipts[idx] = prev_receipts[idx] ? prev_receipts[idx] : 0;
				on_hands[idx] = (idx === 0 ? this.getAllInvItems[index].on_hand : on_hands[idx - 1]) + receipts[idx] - gross_requirements[idx];
			}
			
			for(let idx=0; idx<gross_requirements.length; idx++) {
				let idxAfter = idx + this.getAllItemsMasters[index].lead_time;
				
				net_requirements[idx] = (gross_requirements[idxAfter] ? gross_requirements[idxAfter] : 0) + this.getAllInvItems[index].safe_stock - (on_hands[idxAfter - 1]);
				receipts[idxAfter] = (prev_receipts[idxAfter] ? prev_receipts[idxAfter] : 0) + net_requirements[idx];
				on_hands[idxAfter] = on_hands[idxAfter - 1] + receipts[idxAfter] - (gross_requirements[idxAfter] ? gross_requirements[idxAfter] : 0);

				// Ajusting net requirement
				if(on_hands[idxAfter] > this.getAllInvItems[index].safe_stock || net_requirements[idx] < 0) {					
					net_requirements[idx] = 0
					receipts[idxAfter] = (prev_receipts[idxAfter] ? prev_receipts[idxAfter] : 0);
					on_hands[idxAfter] = on_hands[idxAfter - 1] + receipts[idxAfter] - (gross_requirements[idxAfter] ? gross_requirements[idxAfter] : 0);
				}

				items.push({
					gross_requirement: gross_requirements[idx],
					receipt: receipts[idx],
					on_hand: on_hands[idx],
					net_requirement: net_requirements[idx]
				})
			}
			
			return items
		},

		calculateTotal() {
			this.data.forEach((item) => {
				item.totalInventory = this.totalInventory(item);
				item.averageInventory = this.averageInventory(item);
				item.haulingCost = this.haulingCost(item);
				item.orderCost = this.orderCost(item)
				item.totalCost = this.totalCost(item);
			})
		},

		totalInventory(item) {
			let allOnHands = item.periods.map((period) => period.on_hand)
			let sum = 0
			allOnHands.forEach((value) => {
				sum += value;
			})

			return sum;
		},

		averageInventory(item) {
			return item.totalInventory/item.periods.length
		},

		haulingCost(item) {
			return item.averageInventory * item.carrying_cost;
		},

		orderCost(item) {
			let count = 0

			item.periods.map((period) => period.net_requirement).forEach((value) => {
				if(value > 0) {
					count++
				}
			})

			return count * item.order_cost;
		},

		totalCost(item) {
			return item.haulingCost + item.orderCost
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
		if(isNaN(this.$route.params.report) && this.dataFilesMatch()) {
			this.isValidData = true

			for(let idx = 0; idx < this.getAllBomItems.length; idx++) {
				this.data.push({
					part_number: this.getAllBomItems[idx].part_number,
					yield_percent: this.getAllItemsMasters[idx].yield_percent,
					lead_time: this.getAllItemsMasters[idx].lead_time,
					order_cost: this.getAllItemsMasters[idx].order_cost,
					parent: this.getAllBomItems[idx].parent,
					carrying_cost: this.getAllItemsMasters[idx].carrying_cost,
					qty: this.getAllBomItems[idx].qty,
					lot_size: this.getAllItemsMasters[idx].lot_size,
					factor: "",
					safe_stock: this.getAllInvItems[idx].safe_stock,
					on_hand: this.getAllInvItems[idx].on_hand,
					order: idx,
					periods: this.periodsData(idx)
				})
			}

			this.calculateTotal();
			this.setReportItems(this.data)
		} else if(this.$route.params.report >= 1) {
			this.fetchReport(this.$route.params.report).then(() => {
				this.data = this.report.items;
				this.isValidData = true;
				this.calculateTotal();
			});
		}
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