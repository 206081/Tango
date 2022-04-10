<script>
export default {
  name: "HeaderComponent",
  computed: {
    loggedIn() {
      return this.$store.state.auth.status.loggedIn;
    }
  },
  methods: {
    handleLogout() {
      this.$store.dispatch("auth/logout").then(
        () => {
          this.$router.push("/login")
        }
      );
    }
  }
}
</script>


<template>
  <div class="navbar">
    <div class="logoSection">
      <h2 class="logo" @click="$router.push('/')">
        Tangorello
      </h2>
    </div>
    <div class="navButtons">
      <router-link to="/login" v-if="!loggedIn"><button>Login</button></router-link>
      <button v-on:click="handleLogout" v-else>Logout</button>
    </div>
  </div>
</template>

<style scoped>
  .navbar {
    background: #2c3e50;
    color: white;
    display: flex;
    justify-content: space-between;
    align-items: center;
    z-index: 10;
  }

  .logoSection {
    margin-left: 20px;
  }

  .logo:hover {
    cursor: pointer;
  }

  button {
    border-radius: 5px;
    font-weight: bold;
  }
</style>
