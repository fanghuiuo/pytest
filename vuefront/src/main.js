// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
// 导入全局样式表
import './assets/css/global.css'

import axios from 'axios'

axios.defaults.baseURL = 'http://127.0.0.1:8000'
axios.defaults.headers.common['Authorization'] = ''
// 添加请求拦截器
axios.interceptors.request.use(function (config) {
  // 在发送请求之前做些什么
  // 若token存在，则在每次请求头中加入token
  // 发送请求之前判断是否存在token，除了登录页，其他页面请求头headers都添加token
  console.log(config)
  console.log(localStorage.getItem('token'))
  const pathname = location.pathname
  if (localStorage.getItem('token')) {
    console.log(pathname)
    if (pathname != '/login') {
      config.headers.Authorization = localStorage.getItem('token')
    }
  }
  return config
}, function (error) {
  // 对请求错误做些什么
  return Promise.reject(error);
})

Vue.prototype.$axios = axios

axios.defaults.withCredentials = true
Vue.config.productionTip = false
Vue.use(ElementUI)

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
