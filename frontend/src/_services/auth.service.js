import api from "@/_services/api";
import TokenService from "@/_services/TokenService";

class AuthService {
  login(user) {
    return api
      .post('/api/login/', {
        email: user.email,
        password: user.password
      })
      .then(response => {
        if (response.data.access) {
          TokenService.setUser(response.data);
        }
        return response.data;
      });
  }

  logout() {
    const user = TokenService.getUser()
    return api.post('/api/logout/', {
      refresh: user.refresh,
    }).then(response => {
      TokenService.removeUser();
      return response;
    })
  }

  register(user) {
    return api.post('api/users/register/', {
      first_name: user.firstName,
      last_name: user.lastName,
      email: user.email,
      password: user.password
    });
  }
}
export default new AuthService();
