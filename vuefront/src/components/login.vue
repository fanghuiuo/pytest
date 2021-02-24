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
          { min: 3, max: 12, message: '长度在 3 到 6 个字符', trigger: 'blur' }
        ],
        userpassword: [
          { required: true, message: '请输入密码', trigger: 'blur' },
          { min: 3, max: 12, message: '长度在 3 到 12 个字符', trigger: 'blur' }
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
    login() {
      this.$refs.loginformref.validate((valid) => {
        if (valid) {
          this.$axios({
            method: 'get',
            url: '/api/',
            headers: {
              'Content-Type': 'application/json;charset=UTF-8'
            },
            data: {
              dy: this.loginform.username,
              bj: this.loginform.userpassword
            }
          })
            .then(res => { // 请求成功后执行函数
              if (res.data.message === 'SUCCESS') {
                this.$outer.push('/movie')	// 登录验证成功路由实现跳转
                this.$nortify({
                  title: '提示',
                  message: '用户登录成功',
                  duration: 3000
                });
              } else {
                this.$notify({
                  title: '提示',
                  message: '用户登录失败',
                  duration: 3000
                })
              }
            })
            .catch(err => { // 请求错误后执行函数
              this.$notify({
                title: '提示',
                message: '用户访问错误',
                duration: 3000
              });
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