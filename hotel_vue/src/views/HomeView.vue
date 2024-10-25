<template>
  <div class="home">
    <section class="hero is-medium is-dark mb-6">
      <div class="hero-body has-text-centered">
        <p class="title mb-6">Hotel Picamaderos stay contest</p>
        <p class="subtitle">Do you want to win a stay with us? Fill out the form, and you'll be entered for a chance to win a 2-night, all-inclusive stay at Hotel Picamaderos.</p>
      </div>
    </section>

    <section>
      <div class="has-text-centered">
        <router-link to="/contestant-register" class="button is-primary" >Register for the contest!</router-link>
        <router-link to="/login-contestant" class="button is-link is-focused" v-if="!$store.state.isAuthenticated">Log in contestant Account</router-link>
      </div>
    </section>
 
    <div class="column is-multiline" v-if="isAuthenticated">
      <div class="column is-12">
        <h2 class="is-size-2 has-text-centered">Lastest Contestans</h2>
      </div>
      <div class="column is-3" v-for="contestan in lastestContestants" v-bind:key="contestan.email">
        <h3 class="is-size-4">{{ contestan.email }}</h3>
        <p class="is-size-6 has-text-grey">{{ contestan.first_name }}</p>
        <p class="is-size-6 has-text-grey">{{ contestan.last_name }}</p>
      </div>

    </div>


  </div>
</template>

<script>

import axios from 'axios';
export default {
  name: "HomeView",
  data(){
    return {
      lastestContestants: []
    }
  },
  components: {
  },
  
  computed: {
    isAuthenticated() {
      return !!localStorage.getItem('token');
    },
  }, 
  mounted(){
    this.getLastestContestants()
  },
  methods: {
    getLastestContestants(){
      axios
      .get('/api/v1/lastest-contestans/')
      .then(response => {
        this.lastestContestants = response.data
      })
      .catch(error => {
        console.log(error)
      })
    }
  }
};
</script>
