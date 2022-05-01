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
}

export default new TablesService();
