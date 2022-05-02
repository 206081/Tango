import api from "@/_services/api";

const API_URL = '/api/tables/';

class TablesService {
  async getAllTables() {
    return api.get(API_URL)
      .then(response => {
      return response.data.data
      })
      .catch(error => {
        throw error;
      });
  }
  async getAllLists(tableId) {
    return api.get(API_URL + tableId + '/lists/')
      .then(response => {
        return response.data
      })
      .catch(error => {
        throw error;
      });
  }
  async addTable(tableName) {
    return api.post(API_URL, {"name": tableName})
      .then(response => {
      return response.data.detail;
      })
      .catch(error => {
        throw error;
      });
  }
  async getAllCards(tableId, listId) {
    return api.get(API_URL + tableId + '/lists/' + listId + '/cards/')
      .then(response => {
        return response.data
      })
      .catch(error => {
        throw error;
      });
  }
  async addCard(tableId, listId, cardName) {
    return api.post(API_URL + tableId + '/lists/' + listId + '/cards/', {"name": cardName})
      .then(response => {
        return response.data.detail;
      })
      .catch(error => {
        throw error;
      });
  }
  async addList(tableId, listName) {
    return api.post(API_URL + tableId + '/lists/', {"name": listName})
      .then(response => {
        return response.data.detail;
      })
      .catch(error => {
        throw error;
      });
  }
}

export default new TablesService();
