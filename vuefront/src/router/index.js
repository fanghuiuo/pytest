import Vue from 'vue'
import Router from 'vue-router'
import movie from '@/components/movie'
import login from '@/components/login'


Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      redirect:'/login'
    },
    {
      path: '/movie',
      name: 'movie',
      component: movie
    },
    {
      path: '/login',
      name: 'login',
      component: login
    }
  ]
})
