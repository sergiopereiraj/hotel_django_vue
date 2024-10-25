import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'


axios.defaults.baseURL = 'http://127.0.0.1:8000/'


const token = localStorage.getItem('token');
if (token) {
  store.commit('setToken', token); 
  axios.defaults.headers.common['Authorization'] = `Token ${token}`;
}

createApp(App).use(store).use(router).mount('#app')
