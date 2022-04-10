import axios from 'axios';
class AuthService {
  login(user) {
    return axios
      .post('/api/login/', {
        email: user.email,
        password: user.password
      })
      .then(response => {
        if (response.data.access) {
          localStorage.setItem('user', JSON.stringify(response.data));
        }
        return response.data;
      });
  }

  logout() {
    localStorage.removeItem('user');
  }

  register(user) {
    return axios.post('api/users/register', {
      first_name: user.firstName,
      last_name: user.lastName,
      email: user.email,
      password: user.password
    });
  }
}
export default new AuthService();
