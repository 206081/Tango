<template>
  <Form @submit="handleRegister" :validation-schema="schema" class="form">
    <div v-if="!successful">
      <div class="form-group">
        <label for="firstName">First name</label>
        <Field id="firstName" name="firstName" type="text" class="form-control"/>
        <ErrorMessage name="firstName" class="error-feedback"/>
      </div>
      <div class="form-group">
        <label for="lastName">Last name</label>
        <Field id="lastName" name="lastName" type="text" class="form-control"/>
        <ErrorMessage name="lastName" class="error-feedback"/>
      </div>
      <div class="form-group">
        <label for="email">Email</label>
        <Field id="email" name="email" type="email" class="form-control"/>
        <ErrorMessage name="email" class="error-feedback"/>
      </div>
      <div class="form-group">
        <label for="password">Password</label>
        <Field id="password" name="password" type="password" class="form-control"/>
        <ErrorMessage name="password" class="error-feedback"/>
      </div>
      <div
        v-if="message"
        class="alert"
        :class="successful ? 'alert-success' : 'alert-danger'"
      >
        {{ message }}
      </div>
      <div class="form-group">
        <button class="btn btn-primary btn-block" :disabled="loading">
              <span
                v-show="loading"
                class="spinner-border spinner-border-sm"
              ></span>
          Sign Up
        </button>
      </div>
    </div>
  </Form>
</template>

<script>
import { Form, Field, ErrorMessage } from "vee-validate";
import * as yup from "yup";
export default {
  name: "RegisterPage",
  components: {
    Form,
    Field,
    ErrorMessage,
  },
  data() {
    const schema = yup.object().shape({
      firstName: yup
        .string()
        .required("First name is required!")
        .min(3, "Must be at least 3 characters!")
        .max(20, "Must be maximum 20 characters!"),
      lastName: yup
        .string()
        .required("Last name is required!")
        .min(3, "Must be at least 3 characters!")
        .max(20, "Must be maximum 20 characters!"),
      email: yup
        .string()
        .required("Email is required!")
        .email("Email is invalid!")
        .max(50, "Must be maximum 50 characters!"),
      password: yup
        .string()
        .required("Password is required!")
        .min(6, "Must be at least 6 characters!")
        .max(40, "Must be maximum 40 characters!"),
    });
    return {
      successful: false,
      loading: false,
      message: "",
      schema,
    };
  },
  computed: {
    loggedIn() {
      return this.$store.state.auth.status.loggedIn;
    },
  },
  mounted() {
    if (this.loggedIn) {
      this.$router.push("/profile");
    }
  },
  methods: {
    handleRegister(user) {
      this.message = "";
      this.successful = false;
      this.loading = true;
      this.$store.dispatch("auth/register", user).then(
        (data) => {
          this.message = data.message;
          this.successful = true;
          this.loading = false;
        },
        (error) => {
          this.message =
            (error.response &&
              error.response.data &&
              error.response.data.message) ||
            error.message ||
            error.toString();
          this.successful = false;
          this.loading = false;
        }
      );
    },
  },
};
</script>

<style scoped>
.form {
  background: white;
  padding: 20px;
  height: fit-content;
  border-radius: 20px;
  min-width: 500px;
}

input {
  border: none;
  outline: none;
  border-bottom: 1px solid #ddd;
  font-size: 1em;
  padding: 5px 0;
  margin: 10px 0 5px 0;
  min-width: 240px;
}

button {
  background-color: #3498db;
  padding: 10px 20px;
  margin-top: 10px;
  border: none;
  color: white;
  min-width: 100px;
}

</style>
