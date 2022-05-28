<template>
  <div class="container">
    <div class="card-name">
      {{ data.name }}
      <button class="x-button" @click="onModalClose">x</button>
    </div>
    <span>Assignee: {{ data.assignee }}</span>
    <hr />
    <span>Description:</span>
      <div class="controls" v-if="editDescriptionMode">
        <div>
          <input v-model="localDescription" />
          <button @click="onCancelDescription">Cancel</button>
          <button @click="onSaveDescription">Save</button>
        </div>
      </div>
      <div v-if="!editDescriptionMode">
        <div>{{this.localDescription}}</div>
        <button @click="onEditDescription">Edit</button>
      </div>
    <hr />
      <span>Tasks:</span>
      <div class="task" :key="'task-'+index" v-for="(task, index) of getTasks">
        <span>{{ task.title }}</span>
      </div>
      <div class="controls">
        <div v-if="addTaskMode">
          <div>
            <input v-model="addTaskTitle" />
            <button @click="onCancelTaskClick">Cancel</button>
          </div>
        </div>
        <div>
          <button @click="onAddTaskClick">Add</button>
        </div>
      </div>
    <hr />
    <span>Comments:</span>
    <div class="comment" :key="'comment-'+index" v-for="(comment, index) of getComments">
      <span>{{ comment.text }}</span>
    </div>
    <div class="controls">
      <div v-if="addCommentMode">
        <div>
          <input v-model="addCommentText" />
          <button @click="onCancelCommentClick">Cancel</button>
        </div>
      </div>
      <div>
        <button @click="onAddCommentClick">Add</button>
      </div>
    </div>
  </div>
</template>

<script>
import {closeModal} from "jenesius-vue-modal";
import TablesService from "@/_services/tables.service";
export default {
  name: "CardDetailsComponent",
  props: {
    data: { type: Object },
    ids: { type: Object },
  },
  data() {
    return {
      comments: [...this.data.comments],
      tasks: [...this.data.task],
      localDescription: this.data.description,
      addTaskMode: false,
      addCommentMode: false,
      addTaskTitle: null,
      addCommentText: null,
      editDescriptionMode: false,
    }
  },
  computed: {
    getTasks() {
      return this.tasks;
    },
    getComments() {
      return this.comments;
    }
  },
  methods: {
    onCancelDescription() {
      this.localDescription = this.data.description
      this.editDescriptionMode = false
    },
    onEditDescription() {
      this.editDescriptionMode = true
    },
    async onSaveDescription() {
      if (this.editDescriptionMode) {
        try {
          await TablesService.changeDescription(this.ids.table, this.ids.list, this.data.id, this.localDescription)
        } catch (error) {
          console.log(error)
        } finally {
          this.editDescriptionMode = false;
        }
      } else {
        this.editDescriptionMode = true;
      }
    },
    onModalClose() {
      closeModal()
    },
    onCancelTaskClick() {
      this.addTaskTitle = null;
      this.addTaskMode = false;
    },
    async onAddTaskClick() {
      if (this.addTaskMode) {
        try {
          await TablesService.addTask(this.ids.table, this.ids.list, this.data.id, this.addTaskTitle)
        } catch (error) {
          console.log(error)
        } finally {
          this.tasks.push({title: this.addTaskTitle})
          this.addTaskMode = false;
          this.addTaskTitle = null;
        }
      } else {
        this.addTaskMode = true;
      }
    },
    onCancelCommentClick() {
      this.addCommentText = null;
      this.addCommentMode = false;
    },
    async onAddCommentClick() {
      if (this.addCommentMode) {
        try {
          await TablesService.addComment(this.ids.table, this.ids.list, this.data.id, this.addCommentText)
        } catch (error) {
          console.log(error)
        } finally {
          this.comments.push({text: this.addCommentText});
          this.addCommentMode = false;
          this.addCommentText = null;
        }
      } else {
        this.addCommentMode = true;
      }
    },
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
  .controls {
    display: flex;
    padding-bottom: 10px;
    flex-direction: column;
    align-items: center;
  }
</style>
