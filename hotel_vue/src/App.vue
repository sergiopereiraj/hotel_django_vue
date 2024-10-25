<template>
  <div id="wrapper">
    <nav class="navbar is-dark">
      <div class="navbar-brand">
        <router-link to="/" class="navbar-item">
          <strong>Hotel Picamaderos</strong>
        </router-link>
        <a
          class="navbar-burger"
          aria-label="menu"
          aria-expanded="false"
          data-target="navbar-menu"
          @click="showMobileMenu = ! showMobileMenu">
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>
      <div class="navbar-menu" id="navbar-menu" v-bind:class="{'is-active': showMobileMenu}">
        <div class=" navbar-end">
          <div class="navbar-item">
            <div class="buttons">
              <router-link to="/log-in" class="button" v-if="!$store.state.isAuthenticated">Admin</router-link>
              <router-link to="/my-account" class="button is-danger " v-if="$store.state.isAuthenticated">Log out</router-link>
              <router-link to="/lottery" class="button is-warning" v-if="$store.state.isAuthenticated">Lottery</router-link>
            </div>
          </div>
        </div>
      </div>
    </nav>
    <section class="section">
      <router-view />
    </section>
    <footer class="footer">
      <p class="has-text-centered">Sergio's Company (c) 2024 </p>
    </footer>
  </div>
</template>
<script>
import axios from 'axios';
export default {
  data(){
    return {
      showMobileMenu: false,
    }
  }
}
</script>
<style lang="scss">
@import "../node_modules/bulma";
</style>
