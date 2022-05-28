<template>
  <div class="list-container">
    <div class="list-name">{{ listData.name }}</div>
    <div class="cards-container">
      <div class="card" v-bind:key="card.id" @click="onCardClick(card.id)" v-for="card of cards">
        <span>{{ card.name }}</span>
      </div>
      <div class="controls">
        <div v-if="addCardMode">
          <div>
            <input v-model="addCardName" />
            <button @click="onCancelClick">Cancel</button>
          </div>
        </div>
        <div>
          <button @click="onAddCardClick">Add card</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import TablesService from "@/_services/tables.service";

export default {
  name: "ListComponent",
  props: {
    listData: { type: Object },
    showCardDetails: { type: Function },
  },
  data() {
    return {
      cards: [],
      addCardMode: false,
      addCardName: null,
      cardDetails: {},
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
      this.getCards();
    }
  },
  methods: {
    async getCards() {
      TablesService.getAllCards(this.listData.table.id, this.listData.id).then(cards => {
        this.cards = cards.data;
      })
    },
    onCancelClick() {
      this.addCardName = null;
      this.addCardMode = false;
    },
    async onAddCardClick() {
      if (this.addCardMode) {
        try {
          await TablesService.addCard(this.listData.table.id, this.listData.id, this.addCardName)
        } catch (error) {
          console.log(error)
        } finally {
          await this.getCards()
          this.addCardMode = false;
        }
      } else {
        this.addCardMode = true;
      }
    },
    async onCardClick(cardId) {
      try {
        this.cardDetails = await TablesService.getCardDetails(this.listData.table.id, this.listData.id, cardId)
        this.showCardDetails(this.cardDetails, {table: this.listData.table.id, list: this.listData.id})
      } catch (error) {
        console.log(error)
      }
    }
  }
}
</script>

<style scoped>
 .list-container {
   width: 250px;
   background: whitesmoke;
   flex-wrap: wrap;
 }

 .list-name {
   font-weight: bold;
   text-align: center;
 }

 .cards-container {
   display: flex;
   flex-direction: column;
   gap: 5px;
 }

 .card {
   background-color: white;
   margin: 0 10px;
   text-align: center;
 }

 .controls {
   display: flex;
   padding-bottom: 10px;
   flex-direction: column;
   align-items: center;
 }
</style>
