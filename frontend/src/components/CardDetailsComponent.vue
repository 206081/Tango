<template>
  <div class="container">
    <div class="card-name">
      {{ data.name }}
      <button class="x-button" @click="onModalClose">x</button>
    </div>
    <p>Assignee: {{ data.assignee }}</p>
    <p>Description: {{ data.description }}</p>
  </div>
</template>

<script>
import {closeModal} from "jenesius-vue-modal";
export default {
  name: "CardDetailsComponent",
  props: {
    data: Object
  },
  methods: {
    onModalClose() {
      closeModal()
    }
  }
}
</script>

<style scoped>
  .container {
    max-width: 500px;
    background-color: white;
  }
  .card-name {
    font-weight: bold;
    display: flex;
    align-items: center;
    justify-content: space-between;
  }
  .x-button {
    border: none;
    background: white;
    font-weight: bold;
    color: lightgrey;
  }
</style>
