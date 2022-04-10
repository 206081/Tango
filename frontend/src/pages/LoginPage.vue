<template>
  <div class="form">
    <Form @submit="handleLogin" :validation-schema="schema">
      <div class="form-group">
        <label for="email">e-mail</label>
        <Field id="email" name="email" type="text" class="form-control"/>
        <ErrorMessage name="email" class="error-feedback"/>
      </div>
      <div class="form-group">
        <label for="password">Password</label>
        <Field id="password" name="password" type="password" class="form-control"/>
        <ErrorMessage name="password" class="error-feedback"/>
      </div>
      <div class="form-group">
        <button class="btn btn-primary btn-block" :disabled="loading">
            <span
              v-show="loading"
              class="spinner-border spinner-border-sm"
            ></span>
          <span>Login</span>
        </button>
      </div>
      <div class="form-group">
        <div v-if="message" class="alert alert-danger" role="alert">
          {{ message }}
        </div>
      </div>
    </Form>
    <div class="buttonRow">
      <div class="register">
        <span>Don't have an account?</span>
        <router-link to="/register">
          <button>Register</button>
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
import {Form, Field, ErrorMessage} from "vee-validate";
import * as yup from "yup";

export default {
  name: "LoginPage",
  components: {
    Form,
    Field,
    ErrorMessage,
  },
  data() {
    const schema = yup.object().shape({
      email: yup.string().required("E-mail is required!"),
      password: yup.string().required("Password is required!"),
    });
    return {
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
  created() {
    if (this.loggedIn) {
      this.$router.push("/profile");
    }
  },
  methods: {
    handleLogin(user) {
      this.loading = true;
      this.$store.dispatch("auth/login", user).then(
        () => {
          this.$router.push("/tables");
        },
        (error) => {
          this.loading = false;
          this.message =
            (error.response &&
              error.response.data &&
              error.response.data.message) ||
            error.message ||
            error.toString();
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
  border-radius: 20px;
  min-width: 500px;
  height: fit-content;
}

.emailInput {
  border: none;
  outline: none;
  border-bottom: 1px solid #ddd;
  font-size: 1em;
  padding: 5px 0;
  margin: 10px 0 5px 0;
  width: 100%;
}

input {
  border: none;
  outline: none;
  border-bottom: 1px solid #ddd;
  font-size: 1em;
  padding: 5px 0;
  margin: 10px 0 5px 0;
  width: 95%;
}

button {
  background-color: #3498db;
  padding: 10px 20px;
  margin-top: 10px;
  min-width: 100px;
  border: none;
  color: white;
}

.buttonRow {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.register {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding-top: 20px;
}

</style>
