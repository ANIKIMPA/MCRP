<template>
	<div class="outer">
		<div class="middle">
			<div class="user_card inner">
				<h3 id="form-title">LOGIN</h3>
				<p v-if="errors.detail" class="errornote">{{ errors.detail }}</p>
				<div class="mx-5 form_container">
					<form @submit.prevent="onSubmit">
						<ul>
							<li v-for="(error, i) in errors.email" :key="i" class="errorlist">{{ error }}</li>
						</ul>
						<div class="input-group mb-3">
							<div class="input-group-append">
								<span class="input-group-text"><i class="fas fa-envelope-square"></i></span>
							</div>
							<input type="email" v-model="form.email" placeholder="Email address..." class="form-control" required>
						</div>
						<ul>
							<li v-for="(error, i) in errors.password" :key="i" class="errorlist">{{ error }}</li>
						</ul>
						<div class="input-group mb-2">
							<div class="input-group-append">
								<span class="input-group-text"><i class="fas fa-key"></i></span>
							</div>
							<input type="password" v-model="form.password" placeholder="Password..." required class="form-control">
						</div>

						<div class="d-flex justify-content-center mt-3 login_container">
							<b-button type="submit" class="login_btn" variant="login_btn">Login</b-button>
						</div>
					</form>

				</div>

				<div class="mt-4">
					<div class="d-flex justify-content-center links">
						Don't have an account? <router-link class="ml-2" to="register">Sign Up</router-link>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
import { mapActions } from "vuex";

export default {
	data() {
		return {
			form: {
				email: "",
				password: ""
			},
			errors: {}
		};
	},
	methods: {
		...mapActions(["loginUser"]),
		onSubmit() {
			this.loginUser(this.form)
				.then(() => {
					this.$router.push({ name: "home" });
				})
				.catch(error => {
					this.form.password = "";
					this.errors.detail = "Please correct the error below.";
					this.errors = error;
				});
		}
	}
};
</script>