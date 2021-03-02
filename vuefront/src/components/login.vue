<template>
<div class="login_container">
    <div class="login_box">

        <el-form ref="loginformref" :model="loginform" :rules="loginformrules" label-width="0px" class="login_form">
            <el-form-item prop="username">
              <el-input v-model="loginform.username" prefix-icon="el-icon-user" ref='username'></el-input>
            </el-form-item>
            <el-form-item prop="userpassword">
              <el-input v-model="loginform.userpassword" prefix-icon="el-icon-lock" type="password" ref='userpassword' show-password></el-input>
            </el-form-item>
            <el-form-item class="btns">
              <el-button type="primary" @click="login">登录</el-button>
              <el-button type="info" @click="loginreset">重置</el-button>
            </el-form-item>
        </el-form>

    </div>
</div>

</template>

<script>
export default {
  data() {
    return {
      loginformrules: {
        username: [
          { required: true, message: '请输入用户名', trigger: 'blur' },
          { min: 1, max: 12, message: '长度在 1 到 12个字符', trigger: 'blur' }
        ],
        userpassword: [
          { required: true, message: '请输入密码', trigger: 'blur' },
          { min: 1, max: 12, message: '长度在 1 到 12 个字符', trigger: 'blur' }
        ]
      },
      loginform: {
        username: '1',
        userpassword: '1'
      }
    }
  },
  mounted() {
    // 如果输入框为空聚焦输入框
    if (this.loginform.username === '') {
      this.$refs.username.focus()
    } else if (this.loginform.userpassword === '') {
      this.$refs.userpassword.focus()
    };
  },
  methods: {
    loginreset() {
      this.$refs.loginformref.resetFields()
    },
    // 用于解决CSRF Failed: CSRF token missing or incorrect问题
    getCookie(name) {
      var value = '; ' + document.cookie
      var parts = value.split('; ' + name + '=')
      if (parts.length === 2) return parts.pop().split(';').shift()
      // 解决 eslint Expected to return a value at the end of method 警告
      return true
    },
    login() {
      this.$refs.loginformref.validate((valid) => {
        if (valid) {
          this.$axios({
            method: 'post',
            url: '/login/',
            // 添加headers 用于解决CSRF Failed: CSRF token missing or incorrect问题
            headers: {
              'Content-Type': 'application/json;charset=UTF-8',
              'X-CSRFToken': this.getCookie('csrftoken')
            },
            data: {
              username: this.loginform.username,
              userpassword: this.loginform.userpassword
            }
          })
            .then(res => { // 请求成功后执行函数
              if (res.data.code === 200) {
                console.log(res.data)
                localStorage.setItem('token', res.data.token)
                this.$message({
                  message: '登录成功',
                  type: 'success'
                })
                this.$router.push('movie')	// 登录验证成功路由实现跳转到home页
              } else {
                this.$message({
                  message: '用户名密码不正确 登录失败',
                  type: 'warning'
                })
              }
            })
            .catch(err => { // 请求错误后执行函数
              console.log(err)
              this.$message.error('产生错误')
              console.log(err)
            })
        } else {
          return
        }
      })
    }
  }
}
</script>

<style scoped>
.login_container{
    background-color: #2b4b6b;
    height: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
}
.login_box{
    width: 450px;
    height: 300px;
    background-color: #fff;
    border-radius: 8px; /*圆角 */

}
.btns{
    display: flex;
    justify-content: flex-end;
}
.login_form{
    padding-top: 15%;
    padding-bottom: 10%;
    box-sizing: border-box;
    padding-left: 30px;
    padding-right: 30px;
}
</style>