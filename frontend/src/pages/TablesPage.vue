<template>
  <div class="container">
    <p>temp</p>
    <p>temp</p>
    <div>{{ tables }}</div>
  </div>
</template>

<script>
import TablesService from "@/_services/tables.service";

export default {
  name: "TablesPage",
  components: {},
  data () {
    return {
      tables: []
    }
  },
  computed: {
    loggedIn() {
      return this.$store.state.auth.status.loggedIn;
    },
  },
  mounted() {
    if (!this.loggedIn) {
      this.$router.push('/login');
    } else {
      this.getTables();
    }
  },
  methods: {
    async getTables() {
      TablesService.getAllTables().then(tables =>this.tables = tables)
    }
  }
}
</script>

<style scoped>

</style>
