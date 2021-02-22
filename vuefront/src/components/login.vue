<template>
<div class="login_container">
    <div class="login_box">

        <el-form  label-width="0px" class="login_form">
            <el-form-item >
              <el-input ></el-input>
            </el-form-item>
            <el-form-item >
              <el-input ></el-input>
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
    padding-left: 10px;
    padding-right: 10px;
}
</style>