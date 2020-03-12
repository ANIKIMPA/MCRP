<template>
	<div>
		<b-navbar type="dark" variant="dark" class="shadow-sm">
			<b-navbar-brand href="#" @click="goHome">STORM 5.0</b-navbar-brand>
		</b-navbar>
		<nav class="bg-white border" style="height:50px;">
			<ul id="menu" class="mt-2">
				<li class="parent"><a href="#">File <i class="fas fa-caret-down"></i></a>
					<ul class="child">
							<li v-b-modal.modal-1>New</li>
							<li class="parent">Open... <span class="expand">»</span>
							<ul class="child">
								<BomFilesList />
								<MastFilesList />
								<InvFilesList />
								<ItemMasterFilesList />
							</ul>
						</li>
						<li @click="goHome">Close</li>
						<li @click="newTab">New Tab</li>
						<li @click="closeTab">Close Tab</li>
						<li @click="newWindow">New Window</li>
					</ul>
				</li>
				<li class="parent"><a href="#">Edit <i class="fas fa-caret-down"></i></a>
					<ul class="child">		
						<li>Copy</li>
						<li>Paste</li>
					</ul>
				</li>
				<ReportSetup/>
			</ul>
		</nav>


		<ModuleListModal />
		<DataConfigurationModal @bomFile="saveFile" />
	</div>
</template>

<script>
import ModuleListModal from "./ModuleListModal";
import DataConfigurationModal from "./DataConfigurationModal";
import BomFilesList from "./billOfMaterial/FilesList"
import MastFilesList from "./masterSchedule/FilesList"
import InvFilesList from "./inventoryStatus/FilesList"
import ItemMasterFilesList from "./itemMaster/FilesList"
import ReportSetup from "./report/Setup"
import { mapGetters } from "vuex";
export default {
	components: {
		ModuleListModal,
		DataConfigurationModal,
		BomFilesList,
		MastFilesList,
		InvFilesList,
		ItemMasterFilesList,
		ReportSetup
	},
	data() {
		return {
			createFromBomFile: false,
			fileTypeSelected: ""
		};
	},
	methods: {
		goHome() {
			this.$router.push("/");
		},
		saveFile(fileType) {
			this.fileTypeSelected = fileType
		},
		newTab() {
			window.open("http://localhost:8080/",'_blank');
		},
		closeTab() {
			window.close();
		},
		newWindow() {
			window.open("http://localhost:8080/", "_blank", "toolbar=yes,scrollbars=yes,resizable=yes,top=90,left=500,width=1200,height=800");
		},
		runReport() {

		}
	},
	computed: {
		...mapGetters(["lastOpenedFile"])
	},
};
</script>

<style>
.bg-second {
	background-color: #5e646b;
	color: white !important;
}
.parent {display: block;position: relative;float: left;line-height: 30px;border-right:#CCC 1px solid;}
.parent a{margin: 10px;color: #000000;text-decoration: none;}
.parent:hover > ul {display:block;position:absolute;}
.child {display: none;}
.child li {background-color: #E4EFF7;line-height: 30px;border-bottom:#CCC 1px solid;border-right:#CCC 1px solid; width:100%;}
.child li a{color: #000000;}
ul{list-style: none;margin: 0;padding: 0px; min-width:10em;}
ul ul ul{left: 100%;top: 0;margin-left:1px;}
li:hover {background-color: #95B4CA;}
.parent li:hover {background-color: #F0F0F0;}
li{ cursor: pointer; z-index: 300; }
.expand{font-size:12px;float:right;margin-right:5px;}
</style>
