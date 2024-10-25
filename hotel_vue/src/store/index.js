import { createStore } from "vuex";

export default createStore({
  state: {
    lottery: {
      items: [],
    },
    isAuthenticated: false,
    token: "",
    isLoading: false,
  },
  getters: {},
  mutations: {
    setToken(state, token) {
      state.token = token;
      state.isAuthenticated = true;
    },
    removeToken(state) {
      state.token = ''
      state.isAuthenticated = false
  },
  },
  actions: {},
  modules: {},
});
