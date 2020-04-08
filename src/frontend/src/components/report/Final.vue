<template>
	<div class="row justify-content-between no-gutters">
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
import { mapGetters } from "vuex"

export default {
	name: "FinalReport",
	computed: {
		...mapGetters(["getAllBomItems", "getAllInvItems", "getAllMastItems", "getAllItemsMasters"])
	},
	methods: {
		periods: function(idx) {
			if(idx < this.getAllMastItems.length) {
				return this.getAllMastItems[idx].periods.split(",");
			} else {
				return ["", "", "", "", "", "", "", "", "", ""];
			}
		}
	},
	filters: {
		percentage(value) {
			return parseFloat(value).toFixed(1)+"%";
		},
		dollarFormat(value) {
			return "$" + parseFloat(value).toFixed(2);
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