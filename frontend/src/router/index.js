import { createWebHistory, createRouter } from "vue-router";
import MainPage from "@/pages/MainPage";
import LoginPage from "@/pages/LoginPage";

const routes = [
  {
    path: "/",
    name: "MainPage",
    component: MainPage,
  },
  {
    path: "/login",
    name: "LoginPage",
    component: LoginPage,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
