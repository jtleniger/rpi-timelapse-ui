import Vue from 'vue'
import Router from 'vue-router'
import Intervalometer from './views/Intervalometer.vue'
import Bracketing from './views/Bracketing.vue'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'intervalometer',
      component: Intervalometer
    },
    {
      path: '/bracketing',
      name: 'bracketing',
      component: Bracketing
    }
  ]
})
