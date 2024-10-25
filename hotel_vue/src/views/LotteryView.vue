<template>
  <div class="has-text-centered">
    <h1 class="title is-1">Lottery</h1>
    <hr>
    <button class="button is-warning is-large is-focused" @click="fetchRandomEmail">Get Random Email</button>
    <hr>
    <h1 v-if="email" class= "title is-1">{{ email }}</h1>
    <p v-if="error" class="has-text-danger">{{ error }}</p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: "LotteryView",
  data() {
    return {
      email: '',
      error: ''
    };
  },
  methods: {
    async fetchRandomEmail() {
      this.error = '';
      try {
        const response = await axios.get('/api/v1/api/random-contestant-email/');
        this.email = response.data.email;
      } catch (err) {
        this.error = 'Error fetching email: ' + err.response.data.error;
      }
    }
  }
};
</script>
