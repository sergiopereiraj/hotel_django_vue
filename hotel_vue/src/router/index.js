import { createRouter, createWebHistory } from 'vue-router'
import store from '../store'

import HomeView from '../views/HomeView.vue'
import SignUp from '../views/SignUp.vue'
import LogIn from '../views/LogIn.vue'
import LoginContestant from '../views/LoginContestant.vue'
import MyAccount from '../views/MyAccount.vue'
import LotteryView from '../views/LotteryView.vue'
import ContestantRegister from '../views/ContestantRegister.vue'
import EmailVerification from '../views/EmailVerification.vue'


const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/sign-up',
    name: 'SignUp',
    component: SignUp
  },
  {
    path: '/log-in',
    name: 'LogIn',
    component: LogIn
  },
  {
    path: '/login-contestant',
    name: 'LoginContestant',
    component: LoginContestant
  },
  {
    path: '/verify-email/:token',
    name: 'EmailVerification',
    component: EmailVerification
  },
  {
    path: '/contestant-register',
    name: 'ContestantRegister',
    component: ContestantRegister
  },
  {
    path: '/my-account',
    name: 'MyAccount',
    component: MyAccount,
    meta:{
      requireLogin: true
    }
  },
  {
    path: '/lottery',
    name: 'Lottery',
    component: LotteryView,
    meta:{
      requireLogin: true
    }
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to, from, next) =>{
  if (to.matched.some(record => record.meta.requireLogin) && !store.state.isAuthenticated) {
    next({ name: 'LogIn', query: { to: to.path } });
  } else {
    next()
  }
})

export default router
