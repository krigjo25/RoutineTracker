
//  Importing VueRouter
import { createRouter, createWebHistory } from 'vue-router'


//  Importing Components
import HomeView from '../views/IndexView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
  ],
})

export default router
