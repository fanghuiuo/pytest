<template>
  <el-container class="main-container">
    <el-header >
      <div>
        <span>基础系统</span>
      </div>
      <el-button type="info" round size="small" @click="loginout">退出</el-button>
      </el-header>
    <el-container>
    <el-aside :width="iscollapse ? '64px' : '200px'" >
      <div class="toggle-button" @click="togglecollapse">|||</div>
     <el-menu :unique-opened="true" :router="true"
      background-color="#333744"
      text-color="#fff"
      active-text-color="#409eff" :collapse="iscollapse"
      :collapse-transition="false"
      >
      <!-- 一级菜单 -->
      <el-submenu index="1">
        <!-- 一级菜单模板 -->
        <template slot="title">
          <i class="el-icon-setting"></i>
          <span>用户管理</span>
        </template>
        <!-- 二级菜单 -->
          <el-menu-item index="user" >
          <!-- 二级菜单模板 -->
          <template slot="title">
           <i class="el-icon-user"></i>
           <span>用户列表</span>
          </template>
          </el-menu-item>
      </el-submenu>
      <el-submenu index="2">
        <!-- 一级菜单模板 -->
        <template slot="title">
          <i class="el-icon-video-camera"></i>
          <span>权限管理</span>
        </template>
        <!-- 二级菜单 -->
          <el-menu-item index="permission">
          <!-- 二级菜单模板 -->
          <template slot="title">
           <i class="el-icon-location"></i>
           <span>权限列表</span>
          </template>
          </el-menu-item>
           <!-- 二级菜单 -->
          <el-menu-item index="role">
          <!-- 二级菜单模板 -->
          <template slot="title">
           <i class="el-icon-location"></i>
           <span>角色列表</span>
          </template>
          </el-menu-item>
      </el-submenu>
      <el-submenu index="3">
        <!-- 一级菜单模板 -->
        <template slot="title">
          <i class="el-icon-video-camera"></i>
          <span>豆瓣电影</span>
        </template>
        <!-- 二级菜单 -->
          <el-menu-item index="movie">
          <!-- 二级菜单模板 -->
          <template slot="title">
           <i class="el-icon-location"></i>
           <span>TOP250</span>
          </template>
          </el-menu-item>
      </el-submenu>
    </el-menu>
    </el-aside>

      <el-main>
        <!--路由占位符 -->
        <router-view></router-view>
      </el-main>
    </el-container>
  </el-container>
</template>

<script>
export default {
  data() {
    return {
      // 是否折叠
      iscollapse: false
    }
  },
  methods: {
    loginout() {
      // 清空localStorage
      window.localStorage.clear()
      this.$router.push('/login')
    },
    // 点击按钮 切换菜单折叠
    togglecollapse() {
      this.iscollapse = !this.iscollapse
    }
  }
}
</script>

<style scoped>
  .main-container{
    height: 100%;
  }
  .el-header {
    background-color: #373D41;
    display: flex;
    justify-content: space-between;
    padding-left: 50px; /*字离左边 */
    align-items: center;
    color: #fff;
    font-size: 20px;

    /* text-align: right;
    font-size: 12px;*/
  }
  .el-aside {
    background-color: #333744;
  }
  .el-menu {
    /* 去掉菜单右侧边框线 */
    border-right: none;
  }
  .el-main {
    background-color: #eaedf1;
  }
  /* 折叠栏样式 */
  .toggle-button {
    background-color: #4A5064;
    font-size: 10px;
    line-height: 24px; /* 行高 */
    color: #fff;
    text-align: center;
    letter-spacing: 0.2em;
    cursor: pointer; /* 鼠标放上 变小手 图标 */
  }
</style>