import Vue from 'vue'
import Router from 'vue-router'
import movie from '@/components/movie'
import login from '@/components/login'


Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
<<<<<<< HEAD
      redirect:'/login'
=======
      redirect: '/login'
>>>>>>> 70d5daae15ccda077e59254c053de6646c65244a
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
