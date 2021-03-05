<template>
<div>
  <!-- 面包屑导航区域 -->
      <el-breadcrumb separator-class="el-icon-arrow-right">
        <el-breadcrumb-item :to="{ path: '/home' }">首页</el-breadcrumb-item>
        <el-breadcrumb-item>系统管理</el-breadcrumb-item>
        <el-breadcrumb-item>用户管理</el-breadcrumb-item>
      </el-breadcrumb>
      <el-card class="box-card">
        <el-form :inline="true" :model="formInline" class="demo-form-inline">
          <el-form-item label="电影名">
            <el-input v-model="formInline.dym" placeholder="电影名" clearable></el-input>
          </el-form-item>
          <el-form-item label="类型">
            <el-input v-model="formInline.lx" placeholder="类型" clearable></el-input>
          </el-form-item>
          <el-form-item label="豆瓣标签">
            <el-input v-model="formInline.cybq" placeholder="豆瓣标签" clearable></el-input>
          </el-form-item>
          <el-form-item label="制片国家">
            <el-input v-model="formInline.zpgj" placeholder="制片国家" clearable></el-input>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="getlist">查询</el-button>
          </el-form-item>
        </el-form>
        <el-table :data="info.slice((currentPage-1)*pagesize,currentPage*pagesize)" >
          <el-table-column prop="dym" label="电影名" align="center">
          </el-table-column>
          <el-table-column prop="lx" label="类型" align="center">
          </el-table-column>
          <el-table-column prop="zpgj" label="制片国家" align="center">
          </el-table-column>
          <el-table-column prop="dbpf" label="豆瓣评分" align="center">
          </el-table-column>
          <el-table-column prop="yjhpj" label="一句话评价" align="center">
          </el-table-column>
          <el-table-column prop="imdbpf" label="imdb评分" align="center">
          </el-table-column>
          <el-table-column prop="cybq" label="豆瓣标签" align="center">
          </el-table-column>
        </el-table>
        <el-pagination
            @size-change="handleSizeChange"
            @current-change="handleCurrentChange"
            :current-page="currentPage"
            :page-sizes="[5, 10, 20, 40]"
            :page-size="pagesize"
            layout="total, sizes, prev, pager, next, jumper"
            :total="info.length">    //这是显示总共有多少数据
       </el-pagination>
      </el-card>
</div>
</template>

<script>
export default {
  data() {
    return {
      currentPage: 1, // 初始页
      pagesize: 6, //    每页默认的数据
      totle: 0,
      info: [],
      formInline: {
        dym: '',
        lx: '',
        zpgj: '',
        cybq: ''
      }
    }
  },
  methods: {
    getlist() {
      this.$axios({
        method: 'get',
        url: '/api/',
        params: {
          dym__icontains: this.formInline.dym,
          lx__icontains: this.formInline.lx,
          zpgj__icontains: this.formInline.zpgj,
          cybq__icontains: this.formInline.cybq
        }
      })
        .then((response) => { this.info = response.data })
        .catch(function (error) { // 请求失败处理
          console.log(error);
        })
    },
    // 初始页currentPage、初始每页数据数pagesize和数据data
    handleSizeChange: function (size) {
      this.pagesize = size;
      nsole.log(this.pagesize) // 每页下拉显示数据
    },
    handleCurrentChange: function(currentPage) {
      this.currentPage = currentPage;
      console.log(this.currentPage) // 点击第几页
    },
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