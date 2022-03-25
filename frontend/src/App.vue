<template>
  <HeaderComponent />
  <PageComponent />
  <FooterComponent />
</template>

<script>
import HeaderComponent from "@/components/HeaderComponent";
import FooterComponent from "@/components/FooterComponent";
import PageComponent from "@/components/PageComponent";

export default {
  name: 'App',
  components: {
    PageComponent,
    FooterComponent,
    HeaderComponent,
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
