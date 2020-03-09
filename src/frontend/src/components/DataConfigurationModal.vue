<template>
	<div>
		<b-modal id="data-config" size="lg" title="MRP New Data Configuration">
			<b-row>
				<b-col>
					<b-form-group label="File Type" class="h-92 border p-2">
						<b-form-radio v-model="fileTypeSelected" name="file-type" value="bomModelParameters">Bill of Material</b-form-radio>
						<b-form-radio v-model="fileTypeSelected" name="file-type" value="mastModelParameters">Master Schedule</b-form-radio>
						<b-form-radio v-model="fileTypeSelected" name="file-type" value="invModelParameters">Inventory Status</b-form-radio>
						<b-form-radio v-model="fileTypeSelected" name="file-type" value="itemMasterModelParameters">Item Master</b-form-radio>
						<b-form-radio v-model="fileTypeSelected" name="file-type" value>Resource Capacity</b-form-radio>
					</b-form-group>
				</b-col>
				<b-col cols="8">
					<div v-if="fileTypeSelected != 'bomModelParameters' && fileTypeSelected != ''" class="border p-2 my-3">
						<b-form-group>
							<b-row align-h="between" align-v="center">

								<b-col cols="6">
									<b-form-checkbox v-model="createFromBomFile" :value="true" :unchecked-value="false">Create from BOM file:</b-form-checkbox>
								</b-col>
								<b-col cols="4">
									<SelectBomFile @bomFile="getFileSelected" :createFromBomFile="createFromBomFile" />
								</b-col>
							</b-row>
						</b-form-group>

						<b-form-group>
							<b-form-input :disabled="!createFromBomFile" v-model="fileTitle" readonly></b-form-input>
						</b-form-group>

						<b-form-group label-cols-sm="6" :class="{ disabled: !createFromBomFile }" label="Copy Items:" label-align-sm="left" class="mb-0">
							<b-col cols="12">
								<b-form-radio-group :disabled="!createFromBomFile" :options="['Lowest Level', 'Selected']" />
							</b-col>
						</b-form-group>
					</div>
				</b-col>
			</b-row>

			<template v-slot:modal-footer="{ ok, cancel, close }">
				<b-button variant="secondary" @click="cancel()">Cancel</b-button>
				<b-button v-b-modal.modal-parameters :disabled="createFromBomFile && fileTitle.trim() == '' && fileTypeSelected != 'bomModelParameters'" @click="close()" variant="primary">OK</b-button>
			</template>
		</b-modal>

		<component :is="fileTypeSelected" :createFromBomFile="createFromBomFile"></component>
	</div>
</template>

<script>
import SelectBomFile from "./SelectBomFile";
import { mapGetters } from "vuex";
export default {
	components: {
		SelectBomFile,
		bomModelParameters: () => import("./billOfMaterial/ModelParameters"),
		mastModelParameters: () => import("./masterSchedule/ModelParameters"),
		invModelParameters: () => import("./inventoryStatus/ModelParameters"),
		itemMasterModelParameters: () => import("./itemMaster/ModelParameters"),
	},
	data() {
		return {
			createFromBomFile: false,
			fileTypeSelected: "bomModelParameters",
			fileTitle: ""
		};
	},
	watch: {
		fileTypeSelected: function() {
			if (this.fileTypeSelected.trim() != "") {
				this.$emit("bomFile", this.fileTypeSelected);
			}
		}
	},
	mounted() {
		this.$emit("bomFile", this.fileTypeSelected);
	},
	methods: {
		getFileSelected() {
			this.fileTitle = this.bomFile.title;
		},
		close() {}
	},
	computed: {
		...mapGetters(["bomFile"])
	}
};
</script>

<style scoped>
.h-92 {
	height: 92%;
}
.disabled {
	color: #6c757d;
}
</style>
