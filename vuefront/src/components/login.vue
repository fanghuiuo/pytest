<template>
<div class="login_container">
    <div class="login_box">

<<<<<<< HEAD
        <el-form  label-width="0px" class="login_form">
            <el-form-item >
              <el-input ></el-input>
            </el-form-item>
            <el-form-item >
              <el-input ></el-input>
=======
        <el-form  :model="loginform" :rules="loginformrules" label-width="0px" class="login_form">
            <el-form-item prop="username">
              <el-input v-model="loginform.username" prefix-icon="el-icon-user"></el-input>
            </el-form-item>
            <el-form-item prop="userpassword">
              <el-input v-model="loginform.userpassword" prefix-icon="el-icon-lock" type="password"></el-input>
>>>>>>> 70d5daae15ccda077e59254c053de6646c65244a
            </el-form-item>
            <el-form-item class="btns">
              <el-button type="primary">登录</el-button>
              <el-button type="info">重置</el-button>
            </el-form-item>
        </el-form>

    </div>
</div>

</template>

<script>
export default {
<<<<<<< HEAD

=======
  data() {
    return {
      loginformrules: {
        username: [
          { required: true, message: '请输入用户名', trigger: 'blur' },
          { min: 3, max: 6, message: '长度在 3 到 6 个字符', trigger: 'blur' }
        ],
        userpassword: [
          { required: true, message: '请输入密码', trigger: 'blur' },
          { min: 6, max: 12, message: '长度在 6 到 12 个字符', trigger: 'blur' }
        ]
      },
      loginform: {
        username: '1',
        userpassword: '1'
      }
    }
  }
>>>>>>> 70d5daae15ccda077e59254c053de6646c65244a
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
<<<<<<< HEAD
    padding-left: 10px;
    padding-right: 10px;
=======
    padding-left: 30px;
    padding-right: 30px;
>>>>>>> 70d5daae15ccda077e59254c053de6646c65244a
}
</style>