import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./_store";
import "bootstrap";
import "bootstrap/dist/css/bootstrap.min.css";
import { FontAwesomeIcon } from './plugins/font-awesome'
import setupInterceptors from './_services/setupInterceptors';

setupInterceptors(store);

createApp(App)
  .use(router)
  .use(store)
  .component("font-awesome-icon", FontAwesomeIcon)
  .mount("#app");
