import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import "./plugins/element.js";
import "./assets/css/global.css";
import axios from "axios";

axios.defaults.baseURL = "http://180.76.121.240:8031/api/";
axios.interceptors.request.use(config => {
//   console.log(config)
  config.headers.Authorization = window.sessionStorage.getItem('token')
  return config
})
Vue.prototype.$http = axios.create({
  timeout: 5000,
  async: true,
  crossDomain: true,
  headers: {'Content-type': 'application/x-www-form-urlencoded'}
});

Vue.config.productionTip = false;

new Vue({
  router,
  render: (h) => h(App),
}).$mount("#app");
