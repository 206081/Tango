<template>
  <div class="form">
    <p>
      <input class="emailInput" v-model="state.email" type="email" placeholder="email"/>
      <span v-if="v$.email.$error">
        {{ v$.email.$errors[0].$message }}
      </span>
    </p>
    <div class="doubleInput">
      <p>
        <input class="leftInput" v-model="state.firstName" placeholder="first name"/>
        <span v-if="v$.firstName.$error">
        {{ v$.firstName.$errors[0].$message }}
      </span>
      </p>
      <p>
        <input v-model="state.lastName" placeholder="last name"/>
        <span v-if="v$.firstName.$error">
        {{ v$.lastName.$errors[0].$message }}
      </span>
      </p>
    </div>
    <div class="doubleInput">
      <p>
        <input class="leftInput" v-model="state.password.password" type="password" placeholder="password"/>
        <span v-if="v$.firstName.$error">
        {{ v$.password.password.$errors[0].$message }}
      </span>
      </p>
      <p>
        <input v-model="state.password.confirm" type="password" placeholder="confirm password"/>
        <span v-if="v$.firstName.$error">
        {{ v$.password.confirm.$errors[0].$message }}
      </span>
      </p>
    </div>
    <div class>
      <button @click="submitForm">Submit</button>
    </div>
  </div>
</template>

<script>
import useValidate from "@vuelidate/core";
import {reactive, computed} from "vue";
import {required, email, minLength, sameAs} from "@vuelidate/validators";
import axios from "axios"

export default {
  setup() {
    const state = reactive({
      email: '',
      firstName: '',
      lastName: '',
      password: {
        password: '',
        confirm: '',
      },
    })
    const rules = computed(() => {
      return {
        email: {required, email},
        firstName: {required},
        lastName: {required},
        password: {
          password: {required, minLength: minLength(6)},
          confirm: {required, sameAs: sameAs(state.password.password)},
        },
      };
    })
    const v$ = useValidate(rules, state)

    async function submitForm() {
      this.v$.$validate()
      if (!this.v$.$error) {
        const reqBody = {
          email: state.email,
          password: btoa(state.password.password),
          first_name: state.firstName,
          last_name: state.lastName
        }
        const response = await axios.post('/api/users/register', reqBody)
        console.log(response)
        alert('Form successfully submitted.')
      } else {
        alert('Form failed validation')
      }
    }

    return {state, v$, submitForm}
  },

}
</script>

<style scoped>
.form {
  background: white;
  padding: 20px;
  height: fit-content;
  border-radius: 20px;
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
  border: none;
  color: white;
}

.doubleInput {
  display: flex;
}

.leftInput {
  margin-right: 10px;
}

</style>
