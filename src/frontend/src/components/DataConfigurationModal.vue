<template>
	<div>
		<b-modal id="data-config" size="lg" title="MRP New Data Configuration">
			<b-row>
				<b-col>
					<b-form-group label="File Type" class="h-92 border p-2">
						<b-form-radio v-model="fileTypeSelected" name="file-type" value="bomModelParameters">Bill of Material</b-form-radio>
						<b-form-radio v-model="fileTypeSelected" name="file-type" value="mastModelParameters">Master Schedule</b-form-radio>
						<b-form-radio v-model="fileTypeSelected" name="file-type" value>Inventory Status</b-form-radio>
						<b-form-radio v-model="fileTypeSelected" name="file-type" value>Item Master</b-form-radio>
						<b-form-radio v-model="fileTypeSelected" name="file-type" value>Resource Capacity</b-form-radio>
					</b-form-group>
				</b-col>
				<b-col cols="8">
					<div v-if="
              fileTypeSelected != 'bomModelParameters' && fileTypeSelected != ''" class="border p-2 my-3">
						<b-form-group>
							<b-row align-h="between" align-v="center">

								<b-col cols="6">
									<b-form-checkbox v-model="createFromBomFile" :value="true" :unchecked-value="false">Create from BOM file:</b-form-checkbox>
								</b-col>
								<b-col cols="4">
									<b-button :disabled="!createFromBomFile" variant="outline-secondary" v-b-modal.file-store>Browse...</b-button>
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

			<template v-slot:modal-footer="{ ok, cancel }">
				<b-button variant="secondary" @click="cancel()">Cancel</b-button>
				<b-button v-b-modal.modal-multi-2 variant="primary">OK</b-button>
			</template>
		</b-modal>

		<FileListModal @fileSelected="getFileSelected" />
		<component :is="fileTypeSelected"></component>
	</div>
</template>

<script>
import FileListModal from "./FileListModal";
export default {
	components: {
		FileListModal,
		bomModelParameters: () => import("./billOfMaterial/ModelParameters"),
		mastModelParameters: () => import("./masterSchedule/ModelParameters")
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
				this.$emit("fileSelected", this.fileTypeSelected);
			}
		}
	},
	mounted() {
		this.$emit("fileSelected", this.fileTypeSelected);
	},
	methods: {
		getFileSelected() {
			this.fileTitle = this.$store.state.fileSelected.title;
		}
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
