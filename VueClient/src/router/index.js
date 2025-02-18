// Vue Router

import { createRouter, createWebHistory } from 'vue-router'
import IndexView from '../components/IndexView.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: IndexView
    },
  ]
})

export default router
