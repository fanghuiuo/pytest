import Vue from 'vue'
import Router from 'vue-router'
import movie from '@/components/movie'
import login from '@/components/login'

Vue.use(Router)

const router = new Router({
  routes: [
    {
      path: '/',

      redirect: '/login'
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

// 在路由对象上 挂载路由导航守卫
router.beforeEach((to, from, next) => {
  // to 将要访问的路径
  // from 代表从哪个路径跳转过来
  // next 是一个函数，表示放行
  //  1.next() 放行   2.next('/login') 强制跳转到login

  if (to.path === '/login') return next()// 如果用户访问登录页，直接放行
  const tokenStr = window.localStorage.getItem('token')// 获取token
  if (!tokenStr) return next('/login')// 如果没有token 则强制登录
  next()// 如果用户携带了 token 则放行
  return true
})

export default router
