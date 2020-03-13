<template>
  <b-container>
    <h1>Register Page</h1>

    <b-form @submit.prevent="onSubmit" @reset.prevent="onReset" v-if="show">
      <b-form-group
        label="Email address:"
        label-for="input-1"
        description="We'll never share your email with anyone else."
      >
        <p v-for="(error, i) in form.errors.email" :key="i" class="text-danger">{{ error }}</p>
        <b-form-input
          id="input-1"
          v-model="form.email"
          type="email"
          required
          placeholder="Enter email"
        ></b-form-input>
      </b-form-group>

      <b-form-group label="Password:" label-for="input-2">
        <p v-for="(error, i) in form.errors.password1" :key="i" class="text-danger">{{ error }}</p>
        <b-form-input
          id="input-2"
          v-model="form.password1"
          type="password"
          required
          placeholder="Enter password"
        ></b-form-input>
      </b-form-group>

      <b-form-group label="Password confirmation:" label-for="input-3">
        <p v-for="(error, i) in form.errors.password2" :key="i" class="text-danger">{{ error }}</p>
        <b-form-input id="input-3" v-model="form.password2" type="password" required></b-form-input>
      </b-form-group>

      <b-button type="submit" variant="primary">Submit</b-button>
      <b-button type="reset" variant="danger">Reset</b-button>
    </b-form>
  </b-container>
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
        errors: {}
      },
      show: true
    };
  },
  methods: {
		...mapActions(["registerUser"]),
    onSubmit() {
			this.registerUser(this.form).then(() => {
				this.$router.push({ name: "login" })
			});
    },
    onReset() {
      // Reset our form values
      this.form.email = "";
      this.form.password1 = "";
      this.form.password2 = "";
      this.form.errors = {};
      // Trick to reset/clear native browser form validation state
      this.show = false;
      this.$nextTick(() => {
        this.show = true;
      });
    }
  }
};
</script>