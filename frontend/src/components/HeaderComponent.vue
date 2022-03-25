<script>
export default {
  name: "HeaderComponent"
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
      <router-link to="/login"><button>Login</button></router-link>
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
