<template>
	<div class="outer">
		<div class="middle">
			<div class="user_card inner">
				<h3 id="form-title">REGISTER ACCOUNT</h3>
				<p v-if="errors.detail" class="errornote">{{ errors.detail }}</p>
				<div class="mx-5 form_container">
					<b-form @submit.prevent="onSubmit">
						<b-form-group label-for="email" description="We'll never share your email with anyone else.">
							<ul>
								<li v-for="(error, i) in errors.email" :key="i" class="errorlist">{{ error }}</li>
							</ul>
							<div class="input-group">
								<div class="input-group-append">
									<span class="input-group-text"><i class="fas fa-envelope-square"></i></span>
								</div>
								<b-form-input id="email" v-model="form.email" type="email" placeholder="Email address..." required></b-form-input>
							</div>
						</b-form-group>

						<b-form-group label-for="first_name">
							<ul>
								<li v-for="(error, i) in errors.first_name" :key="i" class="errorlist">{{ error }}</li>
							</ul>
							<div class="input-group">
								<div class="input-group-append">
									<span class="input-group-text"><i class="fas fa-signature"></i></span>
								</div>
								<b-form-input id="first_name" v-model="form.first_name" type="text" placeholder="First name..." required></b-form-input>
							</div>
						</b-form-group>

						<b-form-group label-for="last_name">
							<ul>
								<li v-for="(error, i) in errors.last_name" :key="i" class="errorlist">{{ error }}</li>
							</ul>
							<div class="input-group">
								<div class="input-group-append">
									<span class="input-group-text"><i class="fas fa-signature"></i></span>
								</div>
								<b-form-input id="last_name" v-model="form.last_name" type="text" placeholder="Last name..." required></b-form-input>
							</div>
						</b-form-group>

						<b-form-group label-for="gender">
							<ul>
								<li v-for="(error, i) in errors.gender" :key="i" class="errorlist">{{ error }}</li>
							</ul>
							<div class="input-group">
								<div class="input-group-append">
									<span class="input-group-text"><i class="fas fa-venus-mars"></i></span>
								</div>
								<b-form-select id="gender" v-model="form.gender" :options="choices" required></b-form-select>
							</div>
						</b-form-group>

						<b-form-group label-for="password1" description="Your password can’t be too similar to your other personal information.">
							<ul>
								<li v-for="(error, i) in errors.password1" :key="i" class="errorlist">{{ error }}</li>
							</ul>
							<div class="input-group">
								<div class="input-group-append">
									<span class="input-group-text"><i class="fas fa-key"></i></span>
								</div>
								<b-form-input id="password1" v-model="form.password1" type="password" placeholder="Password..." required></b-form-input>
							</div>
						</b-form-group>
						
						<b-form-group label-for="password2" description="Enter the same password as before, for verification.">
							<ul>
								<li v-for="(error, i) in errors.password2" :key="i" class="errorlist">{{ error }}</li>
							</ul>
							<div class="input-group">
								<div class="input-group-append">
									<span class="input-group-text"><i class="fas fa-key"></i></span>
								</div>
								<b-form-input id="password2" v-model="form.password2" type="password" placeholder="Password confirmation..." required></b-form-input>
							</div>
						</b-form-group>

						<div class="d-flex justify-content-center mt-3 login_container">
							<b-button type="submit" class="login_btn" variant="login_btn">Register</b-button>
						</div>
					</b-form>

				</div>

				<div class="mt-4">
					<div class="d-flex justify-content-center links">
						Already have an account? <router-link class="ml-2 link" to="login">Login</router-link>
					</div>
				</div>
			</div>
		</div>
	</div>
	<!-- <b-container>
		<h1>Register Page</h1>

		<b-form @submit.prevent="onSubmit" @reset.prevent="onReset" v-if="show">
			<b-form-group label="Email address:" label-for="input-1" description="We'll never share your email with anyone else.">
				<p v-for="(error, i) in errors.email" :key="i" class="text-danger">{{ error }}</p>
				<b-form-input id="input-1" v-model="form.email" type="email" required placeholder="Enter email"></b-form-input>
			</b-form-group>

			<b-form-group label="Password:" label-for="input-2">
				<p v-for="(error, i) in errors.password1" :key="i" class="text-danger">{{ error }}</p>
				<b-form-input id="input-2" v-model="form.password1" type="password" required placeholder="Enter password"></b-form-input>
			</b-form-group>

			<b-form-group label="Password confirmation:" label-for="input-3">
				<p v-for="(error, i) in errors.password2" :key="i" class="text-danger">{{ error }}</p>
				<b-form-input id="input-3" v-model="form.password2" type="password" required></b-form-input>
			</b-form-group>

			<b-button type="submit" variant="primary">Submit</b-button>
			<b-button type="reset" variant="danger">Reset</b-button>
		</b-form>
	</b-container> -->
</template>

<script>
import { mapActions } from "vuex";

export default {
	name: "Register",
	data() {
		return {
			form: {
				email: "",
				password1: "",
				password2: "",
				first_name: "",
				last_name: "",
				gender: null
			},
			choices: [
				{ value: null, text: "Gender...", disabled: true },
				{ value: "M", text: "Male" },
				{ value: "F", text: "Female" }
			],
			errors: {},
			show: true
		};
	},
	methods: {
		...mapActions(["registerUser"]),
		onSubmit() {
			this.registerUser(this.form)
				.then(() => {
					this.$router.push({ name: "login" });
				})
				.catch(error => {
					this.errors = error;
					this.errors.detail = "Please correct the error below.";
				});
		},
		reset() {
			this.form.password1 = "";
			this.form.password2 = "";
		}
	}
};
</script>