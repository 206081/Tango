<template>
  <HeaderComponent />
  <PageComponent />
  <FooterComponent />
</template>

<script>
import HeaderComponent from "@/components/HeaderComponent";
import FooterComponent from "@/components/FooterComponent";
import PageComponent from "@/components/PageComponent";
import eventBus from "@/_common/EventBus";
import 'vue-next-select/dist/index.min.css'

export default {
  name: 'App',
  components: {
    PageComponent,
    FooterComponent,
    HeaderComponent,
  },
  methods: {
    logOut() {
      this.$store.dispatch('auth/logout');
      this.$router.push('/login');
    }
  },
  mounted() {
    eventBus.on("logout", () => {
      this.logOut();
    });
  },
  beforeUnmount() {
    eventBus.remove("logout");
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  background: lightgray;
  display: flex;
  flex-direction: column;
  height: 100%;
  width: 100%;
}

html, body {
  height:100%; /*both html and body*/
}

body {
  margin: 0; /*reset default margin*/
}

button:hover {
  cursor: pointer;
}
</style>
