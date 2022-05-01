import api from "@/_services/api";

const API_URL = '/api/tables/';
class TablesService {
  getAllTables() {
    return api.get(API_URL);
  }
}
export default new TablesService();
