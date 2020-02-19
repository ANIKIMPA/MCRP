<template>
	<div>
		<b-navbar type="dark" variant="dark" class="shadow-sm">
			<b-navbar-brand href="#" @click="goHome">STORM 5.0</b-navbar-brand>
		</b-navbar>
		<nav class="bg-white border" style="height:50px;">
			<!-- <b-dropdown id="dropdown-left" text="File" variant="white" class="m-2">
				<b-dropdown-item v-b-modal.modal-1 href="#">New </b-dropdown-item>
				<b-dropdown-item href="#">Open...</b-dropdown-item>
				<b-dropdown-item href="#" @click="goHome">Close</b-dropdown-item>
				<b-dropdown-item href="#">Close All</b-dropdown-item>
				<b-dropdown-item href="#">New Window</b-dropdown-item>
			</b-dropdown>

			<b-dropdown id="dropdown-right" right text="Edit" variant="white" class="m-2">
				<b-dropdown-item href="#">Copy</b-dropdown-item>
				<b-dropdown-item href="#">Paste</b-dropdown-item>
			</b-dropdown> -->
			<ul id="menu" class="mt-2">
				<li class="parent"><a href="#">File <i class="fas fa-caret-down"></i></a>
					<ul class="child">
							<li v-b-modal.modal-1>New</li>
							<li class="parent">Open... <span class="expand">»</span>
							<ul class="child">
								<BomFilesList />
								<li>MAST Files</li>
							</ul>
						</li>
						<li @click="goHome">Close</li>
						<li>Close All</li>
						<li>New Window</li>
					</ul>
				</li>
				<li class="parent"><a href="#">Edit <i class="fas fa-caret-down"></i></a>
					<ul class="child">			
						<li>Copy</li>
						<li>Paste</li>
					</ul>
				</li>
			</ul>
		</nav>


		<ModuleListModal />
		<DataConfigurationModal @bomFile="saveFile" />
	</div>
</template>

<script>
import ModuleListModal from "./ModuleListModal";
import DataConfigurationModal from "./DataConfigurationModal";
import BomFilesList from "./billOfMaterial/BomFilesList"
export default {
	components: {
		ModuleListModal,
		DataConfigurationModal,
		BomFilesList
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
		}
	}
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
li{ cursor: pointer; }
.expand{font-size:12px;float:right;margin-right:5px;}
</style>
