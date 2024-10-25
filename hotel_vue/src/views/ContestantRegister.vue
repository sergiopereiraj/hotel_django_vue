<template>
    <div class="has-text-centered">
      <h1 class="title is-1">Register for the Contest</h1>
      <form @submit.prevent="registerContestant">
        <div class="field">
          <label class="label">Email</label>
          <div class="control">
            <input type="email" v-model="contestant.email" class="input" required />
          </div>
        </div>
        <div class="field">
          <label class="label">First Name</label>
          <div class="control">
            <input type="text" v-model="contestant.first_name" class="input" required />
          </div>
        </div>
        <div class="field">
          <label class="label">Last Name</label>
          <div class="control">
            <input type="text" v-model="contestant.last_name" class="input" required />
          </div>
        </div>
        <div class="field">
          <label class="label">Password</label>
          <div class="control">
            <input type="password" v-model="contestant.password" class="input" required />
          </div>
        </div>
        <button type="submit" class="button is-primary">Register</button>
      </form>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    name: 'ContestantRegister',
    data() {
      return {
        contestant: {
          email: '',
          first_name: '',
          last_name: '',
          password: '',
        },
      };
    },
    methods: {
      async registerContestant() {
        try {
          const response = await axios.post('/api/v1/contestants/register/', this.contestant); 
          console.log(response.data);
          
          alert('Registration is ready!!, now you must confirm your Email, check in your email');
        } catch (error) {
          console.error('Error registering contestant:', error);
          alert('Oh! we have a problem, please try again');
        }
      },
    },
  };
  </script>

  