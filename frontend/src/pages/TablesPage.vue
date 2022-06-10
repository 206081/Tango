<template>
  <div class="tables-container">
    <div class="controls">
      <div v-if="addTableMode">
        <input v-model="addTableName" />
        <button @click="onCancelClick">Cancel</button>
      </div>
      <VueSelect v-else class="select" v-model="selectedTable" :options="tables" label-by="name" placeholder="Select table" close-on-select/>
      <button @click="onAddTableClick">Add table</button>
    </div>
    <div v-if="selectedTable && users && users?.length > 0" class="controls">
      <div v-if="inviteUserMode">
        <VueSelect class="select" v-model="selectedUser" :options="users" label-by="name" placeholder="Invite user" close-on-select/>
        <button @click="onInviteCancel">Cancel</button>
      </div>
      <button @click="onInviteClick">Invite user</button>
    </div>
    <div class="lists-container">
      <div v-bind:key="list.id" v-for="list of lists">
        <ListComponent :show-card-details="openDialog"  :list-data="list" />
      </div>
      <div v-if="selectedTable" class="controls">
        <div v-if="addListMode">
          <input v-model="addListName" />
          <button @click="onCancelListClick">Cancel</button>
        </div>
        <div>
          <button @click="onAddListClick">Add list</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import TablesService from "@/_services/tables.service";
import ListComponent from "@/components/ListComponent";
import VueSelect from 'vue-next-select'
import CardDetailsComponent from "@/components/CardDetailsComponent";
import {openModal} from "jenesius-vue-modal";

export default {
  name: "TablesPage",
  components: {ListComponent, VueSelect},
  data() {
    return {
      addTableMode: false,
      addTableName: null,
      inviteUserMode: null,
      addListMode: false,
      addListName: null,
      selectedTable: null,
      selectedUser: null,
      tables: [],
      lists: [],
      users: [],
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
  watch: {
    selectedTable(value) {
      this.getLists(value.id)
      this.onCancelClick();
      this.onCancelListClick();
      this.onInviteCancel();
      this.getUsers();
    },
  },
  methods: {
    async getUsers() {
      TablesService.getUsers().then(users => {
        const currentTable = JSON.parse(JSON.stringify(this.selectedTable))
        this.users = users.filter((el) => !currentTable?.members?.includes(el.id))
      })
    },
    async getTables() {
      TablesService.getAllTables().then(tables => {
        this.tables = tables
      })
    },
    async getLists(tableId) {
      TablesService.getAllLists(tableId).then(lists => {
        this.lists = lists.data
      })
    },
    onCancelClick() {
      this.addTableName = null;
      this.addTableMode = false;
    },
    onInviteCancel() {
      this.inviteUserMode = false;
      this.selectedUser = null;
    },
    async onAddTableClick() {
      if (this.addTableMode) {
        try {
          await TablesService.addTable(this.addTableName)
        } catch (error) {
          console.log(error)
        } finally {
          await this.getTables()
          this.addTableMode = false;
        }
      } else {
        this.addTableMode = true;
      }
    },
    async onInviteClick() {
      if (this.inviteUserMode) {
        try {
          await TablesService.addUserToTable(this.selectedTable.id, this.selectedTable.members, this.selectedUser.id).then(() => {
            this.users = null;
            this.selectedUser = null;
            this.getUsers();
          })
        } catch (error) {
          console.log(error)
        } finally {
          this.inviteUserMode = false;
        }
      } else {
        this.inviteUserMode = true;
      }
    },
    onCancelListClick() {
      this.addListName = null;
      this.addListMode = false;
    },
    async onAddListClick() {
      if (this.addListMode) {
        try {
          await TablesService.addList(this.selectedTable.id, this.addListName)
        } catch (error) {
          console.log(error)
        } finally {
          await this.getLists(this.selectedTable.id)
          this.addListMode = false;
        }
      } else {
        this.addListMode = true;
      }
    },
    openDialog(dialogData, ids, onTaskPush, onCommentPush) {
      openModal(CardDetailsComponent, {
        data: dialogData,
        ids,
        onTaskPush,
        onCommentPush
      })
    }
  }
}
</script>

<style scoped>
  .tables-container {
    margin-top: 20px;
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  .controls {
    display: flex;
    padding-bottom: 10px;
  }

  .select {
    background-color: white;
  }

  .lists-container {
    display: flex;
    gap: 15px;
  }
</style>
