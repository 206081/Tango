import api from "@/_services/api";

const API_URL = '/api/tables/';

class TablesService {
  async getUsers() {
    return api.get ('/api/users/').then(response => {
      return response.data.map((res) => {
        return {
          id: res.id,
          name: res.full_name,
        }
      })
    })
      .catch(error => {
        throw error;
      })
  }
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
  async addUserToTable(tableId, currentMembers, userId) {
    return api.patch(API_URL + tableId + '/', {"members": [...currentMembers, userId]})
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
  async changeDescription(tableId, listId, cardId, newDesc) {
    return api.patch(API_URL + tableId + '/lists/' + listId + '/cards/' + cardId + '/', {"description": newDesc})
      .then(response => {
        return response.data.detail;
      })
      .catch(error => {
        throw error;
      });
  }
  async addTask(tableId, listId, cardId, task) {
    return api.post(API_URL + tableId + '/lists/' + listId + '/cards/' + cardId + '/tasks/', {"title": task})
      .then(response => {
        return response.data.detail;
      })
      .catch(error => {
        throw error;
      });
  }
  async addComment(tableId, listId, cardId, comment) {
    return api.post(API_URL + tableId + '/lists/' + listId + '/cards/' + cardId + '/comments/', {"text": comment})
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
  async getCardDetails(tableId, listId, cardId) {
    return api.get(API_URL + tableId + '/lists/' + listId + '/cards/' + cardId + '/')
      .then(response => {
        return response.data.data
      })
      .catch(error => {
        throw error;
      });
  }
}

export default new TablesService();
