<template>
	<div>
		<b-navbar toggleable="lg" type="dark" variant="dark" class="shadow-sm">
			<b-navbar-brand href="#" @click="goHome" class="p-0"><img src="../assets/img/logo_mcrp_transparent.png" width="50px" alt="LOGO"> MCRP</b-navbar-brand>
			<b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

			<b-collapse id="nav-collapse" is-nav>
				<!-- Right aligned nav items -->
				<b-navbar-nav class="ml-auto">
					<b-nav-form>
						<b-form-input size="sm" class="mr-sm-2" placeholder="Search"></b-form-input>
						<b-button size="sm" class="my-2 my-sm-0" type="submit">Search</b-button>
					</b-nav-form>

					<b-nav-item-dropdown right>
						<!-- Using 'button-content' slot -->
						<template v-slot:button-content>
							<em><i class="fas fa-user-circle"></i></em>
						</template>
						<b-dropdown-item disabled>Hi, {{ getUser.first_name }} {{ getUser.last_name }}</b-dropdown-item>
						<b-dropdown-divider></b-dropdown-divider>
						<b-dropdown-item @click="showProfile">My Profile</b-dropdown-item>
						<b-dropdown-item @click="showProfile">Change Password</b-dropdown-item>
						<b-dropdown-item @click.prevent="logOut">Sign Out</b-dropdown-item>
					</b-nav-item-dropdown>
				</b-navbar-nav>
			</b-collapse>
		</b-navbar>
		<nav class="bg-nav" style="height:50px;">
			<ul id="menu" class="pt-2">
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
						<li @click="saveReport">Save</li>
						<li @click="goHome">Close</li>
						<li @click="newTab">New Tab</li>
						<li @click="closeTab">Close Tab</li>
						<li @click="newWindow">New Window</li>
					</ul>
				</li>
				<li class="parent"><a href="#">Report <i class="fas fa-caret-down"></i></a>
					<ul class="child">
						<ReportSetup />
						<li class="parent">Open... <span class="expand">»</span>
							<ul class="child">
								<SelectReport />
							</ul>
						</li>
						<li v-if="$route.name === 'final_report'">
							<a href="#" @click.prevent="exportExcel">Export to Excel</a>
						</li>
					</ul>
				</li>
			</ul>
		</nav>

		<ModuleListModal />
		<DataConfigurationModal @bomFile="saveFile" />
		<SaveReportModal/>
	</div>
</template>

<script>
import ModuleListModal from "./ModuleListModal";
import DataConfigurationModal from "./DataConfigurationModal";
import BomFilesList from "./billOfMaterial/FilesList";
import MastFilesList from "./masterSchedule/FilesList";
import InvFilesList from "./inventoryStatus/FilesList";
import ItemMasterFilesList from "./itemMaster/FilesList";
import SaveReportModal from "./report/SaveReportModal";
import ReportSetup from "./report/Setup";
import SelectReport from "./report/SelectReport";
import { mapGetters, mapActions } from "vuex";
export default {
	components: {
		ModuleListModal,
		DataConfigurationModal,
		BomFilesList,
		MastFilesList,
		InvFilesList,
		ItemMasterFilesList,
		ReportSetup,
		SaveReportModal,
		SelectReport
	},
	data() {
		return {
			createFromBomFile: false,
			fileTypeSelected: ""
		};
	},
	onIdle() {
		// dispatch logoutUser if no activity detected
		this.logoutUser().then(() => {
			this.$router.push("login");
		});
	},
	methods: {
		...mapActions(["logoutUser", "updateReport", "fetchUserProfile"]),
		goHome() {
			this.$router.push("/");
		},
		saveFile(fileType) {
			this.fileTypeSelected = fileType;
		},
		newTab() {
			window.open("http://localhost:8080/", "_blank");
		},
		closeTab() {
			window.close();
		},
		newWindow() {
			window.open(
				"http://localhost:8080/",
				"_blank",
				"toolbar=yes,scrollbars=yes,resizable=yes,top=90,left=500,width=1200,height=800"
			);
		},
		logOut() {
			this.logoutUser().then(() => {
				this.$router.push({
					name: "login"
				});
			});
		},
		saveReport() {
			if(this.$route.name === "final_report") {
				if(isNaN(this.report.id) || this.report.id <= 0) {
					this.$bvModal.show('save-report');
				}
			}
		},
		exportExcel() {
			if(this.report.id && this.report.id >= 1) {
				window.location.href = `http://localhost:8000/export/report-xls/${this.report.id}`;
			} else {
				this.saveReport();
			}
		},
		showProfile() {
			this.$router.push({
				name: "profile"
			});
		}
	},
	computed: {
		...mapGetters(["getUser","report"])
	},
	mounted() {
		this.fetchUserProfile();
	}
};
</script>

<style>
.bg-second {
	background-color: #5e646b;
	color: white !important;
}
.parent {
	display: block;
	position: relative;
	float: left;
	line-height: 30px;
	border-right: #ccc 1px solid;
}
.parent a {
	margin: 10px;
	color: #000000;
	text-decoration: none;
}
.parent:hover > ul {
	display: block;
	position: absolute;
}
.child {
	display: none;
}
.child li {
	background-color: #e4eff7;
	line-height: 30px;
	border-bottom: #ccc 1px solid;
	border-right: #ccc 1px solid;
	width: 100%;
}
.child li a {
	color: #000000;
}
ul {
	list-style: none;
	margin: 0;
	padding: 0px;
	min-width: 10em;
}
ul ul ul {
	left: 100%;
	top: 0;
	margin-left: 1px;
}
ul#menu li:hover {
	background-color: #95b4ca;
}
.parent li:hover {
	background-color: #f0f0f0;
}
ul#menu li {
	cursor: pointer;
	z-index: 300;
}
.expand {
	font-size: 12px;
	float: right;
	margin-right: 5px;
}
</style>
