<template>
  <div class="email-verification">
    <h1 class="title is-2">Email Verification</h1>

    <div v-if="emailVerified">
      <h2>Your email has been verified. Please set your password.</h2>
      <form @submit.prevent="setPassword">
        <input
          class="input is-link"
          type="password"
          v-model="password"
          placeholder="Enter new password"
          required
        />
        <button class="button is-link" type="submit">Set Password</button>
      </form>
    </div>

    <div v-else>
      <h2 class="title is-5">Verifying your email...</h2>
    </div>

    <div v-if="errorMessage">
      <p>{{ errorMessage }}</p>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "EmailVerification",
  data() {
    return {
      emailVerified: false,
      password: "",
      errorMessage: "",
    };
  },
  methods: {
    async verifyEmail() {
      const token = this.$route.params.token;

      try {
        const response = await axios.get(`/api/v1/verify-email/${token}`);
        if (response.data.message.includes("verified successfully")) {
          this.emailVerified = true;
          this.email = response.data.email;
        } else {
          this.errorMessage = "Email verification failed";
        }
      } catch (error) {
        this.errorMessage =
          error.response.data.error || "Error during verification";
      }
    },
    async setPassword() {
      const email = this.$route.query.email;

      try {
        const response = await axios.post(
          "http://localhost:8000/api/v1/set-password/",
          {
            email: this.email,
            password: this.password,
          }
        );

        if (response.data.message === "Password set successfully") {
          alert("Password set successfully. You can now log in.");
          this.$router.push("/login");
        } else {
          this.errorMessage = "Failed to set password";
        }
      } catch (error) {
        this.errorMessage =
          error.response.data.error || "Error setting password";
      }
    },
  },
  mounted() {
    this.verifyEmail();
  },
};
</script>

<style scoped>
.email-verification {
  max-width: 400px;
  margin: 0 auto;
  padding: 20px;
  text-align: center;
}
</style>
