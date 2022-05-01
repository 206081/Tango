<template>
  <div>WIP</div>
</template>

<script>
import TablesService from "@/_services/tables.service";

export default {
  name: "TablesPage",
  components: {},
  data () {},
  computed: {
    loggedIn() {
      return this.$store.state.auth.status.loggedIn;
    },
  },
  mounted() {
    if (this.loggedIn) {
      this.getTables()
    }
  },
  methods: {
    getTables() {
      const resp = TablesService.getAllTables()
      console.log('resp ', resp.data)
    }
  }
}
</script>

<style scoped>

</style>
