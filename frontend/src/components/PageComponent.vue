<template>
  <div class="page">
    <router-view />
  </div>
</template>

<script>
export default {
  name: "PageComponent"
}
</script>

<style scoped>
  .page {
    display: flex;
    flex-grow: 1;
    align-self: center;
  }
</style>
