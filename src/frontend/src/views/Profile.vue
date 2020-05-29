<template>
	<div class="container">
		<div class="row">
			<div class="col-sm-3 mt-3" role="navigation">
				<b-card-group deck>
					<b-card class="text-left">
						<b-card-text>
							<ul>
								<li role="presentation">
									<ul>
										<li><a href=""><i class="fa fa-chevron-right fa-fw"></i> My Profile</a></li>
										<li><a href=""><i class="fa fa-chevron-right fa-fw"></i> Change Password</a></li>
										<li><a href="#" @click.prevent="logOut"><i class="fa fa-chevron-right fa-fw"></i> Sign Out</a></li>
									</ul>
								</li>
							</ul>
						</b-card-text>
					</b-card>
				</b-card-group>
			</div>

			<div class="col-sm-9 mt-3">
				<div class="section-banner img-responsive rounded" alt="My Account">
					<h1 class="text-right th-banner">My Account</h1>
				</div>
				<h2 class="text-left mb-3">My Profile</h2>

				<b-form @submit.prevent="onSubmit">
					<b-form-group label-for="email" label="Email" description="Please use valid UPR email.">
						<ul>
							<li v-for="(error, i) in errors.email" :key="i" class="errorlist">{{ error }}</li>
						</ul>
						<div class="input-group">
							<div class="input-group-append">
								<span class="input-group-text"><i class="fas fa-envelope-square"></i></span>
							</div>
							<b-form-input id="email" v-model="form.email" type="email" placeholder="Enter your email address..." required></b-form-input>
						</div>
					</b-form-group>

					<b-form-group label="First name" label-for="first_name">
						<ul>
							<li v-for="(error, i) in errors.first_name" :key="i" class="errorlist">{{ error }}</li>
						</ul>
						<div class="input-group">
							<div class="input-group-append">
								<span class="input-group-text"><i class="fas fa-signature"></i></span>
							</div>
							<b-form-input id="first_name" v-model="form.first_name" type="text" placeholder="Enter your first name..." required></b-form-input>
						</div>
					</b-form-group>

					<b-form-group label="Last name" label-for="last_name">
						<ul>
							<li v-for="(error, i) in errors.last_name" :key="i" class="errorlist">{{ error }}</li>
						</ul>
						<div class="input-group">
							<div class="input-group-append">
								<span class="input-group-text"><i class="fas fa-signature"></i></span>
							</div>
							<b-form-input id="last_name" v-model="form.last_name" type="text" placeholder="Enter your last name..." required></b-form-input>
						</div>
					</b-form-group>

					<div class="mt-3 text-right">
						<b-button type="submit" variant="primary">Save</b-button>
					</div>
				</b-form>
			</div>
		</div>
	</div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
export default {
	name: "Profile",
	data() {
		return {
			form: {
				email: "",
				first_name: "",
				last_name: ""
			},
			errors: {
				email: "",
				first_name: "",
				last_name: ""
			}
		};
	},
	computed: {
		...mapGetters(["getUser"])
	},
	methods: {
		...mapActions(["logoutUser", "updateUserProfile"]),
		onSubmit() {
			this.updateUserProfile(this.form).then(() => {
				this.$bvToast.show("saved-toast");
			});
		},
		logOut() {
			this.logoutUser().then(() => {
				this.$router.push({
					name: "login"
				});
			});
		}
	},
	mounted() {
		this.form = {
			email: this.getUser.email,
			first_name: this.getUser.first_name,
			last_name: this.getUser.last_name
		};
	}
};
</script>

<style>
.form-group {
	text-align: left;
}
.img-responsive {
	display: block;
	max-width: 100%;
	height: 150px;
	background-size: auto 100%;
	background-image: url("../assets/img/user-profile.jpg");
	background-repeat: repeat-x;
	margin-bottom: 8px;
}
.th-banner {
	position: relative;
	top: 30%;
	width: 70%;
}
</style>