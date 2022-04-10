import axios from 'axios';
import authHeader from './auth-header';
const API_URL = '/api/tables/';
class TablesService {
  getAllTables() {
    return axios.get(API_URL, { headers: authHeader() });
  }
}
export default new TablesService();
