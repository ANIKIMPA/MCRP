<template>
  <b-container>
    <h1>Login Page</h1>

    <h3 v-if="wrongCred">Wrong credentials entered!. Please enter your correct details.</h3>

    <b-form @submit.prevent="onSubmit" @reset.prevent="onReset" v-if="show">
      <b-form-group label="Email address:" label-for="input-email">
        <b-form-input
          id="input-email"
          v-model="form.email"
          type="email"
          required
          placeholder="Enter email"
        ></b-form-input>
      </b-form-group>

      <b-form-group label="Password:" label-for="input-password">
        <b-form-input id="input-password" type="password" v-model="form.password" required></b-form-input>
      </b-form-group>

      <b-button type="submit" variant="primary">Submit</b-button>
      <b-button type="reset" variant="danger">Reset</b-button>
    </b-form>
  </b-container>
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
      show: true,
      wrongCred: false
    };
  },
  methods: {
    ...mapActions(["loginUser"]),
    onSubmit() {
      this.loginUser(this.form)
        .then(() => {
          this.wrongCred = false;
          this.$router.push({ name: "downloads" });
        })
        .catch(error => {
          console.log(error);
          this.wrongCred = true;
        });
    },
    onReset() {
      // Reset our form values
      this.form.email = "";
      this.form.name = "";
      this.form.food = null;
      this.form.checked = [];
      // Trick to reset/clear native browser form validation state
      this.show = false;
      this.$nextTick(() => {
        this.show = true;
      });
    }
  }
};
</script>