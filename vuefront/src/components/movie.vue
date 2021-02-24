<template>
  <el-container class="main-container">
    <el-header >
      <div>
        <span>基础系统</span>
      </div>
      <el-button type="info" round size="small"  >退出</el-button>
      </el-header>
    <el-container>
      <el-aside width="200px" >
     <el-menu
      background-color="#333744"
      text-color="#fff"
      active-text-color="#ffd04b">
      <!-- 一级菜单 -->
      <el-submenu index="1">
        <!-- 一级菜单模板 -->
        <template slot="title">
          <i class="el-icon-location"></i>
          <span>导航一</span>
        </template>
        <!-- 二级菜单 -->
        <el-menu-item index="1-1">
          <!-- 二级菜单模板 -->
          <template slot="title">
           <i class="el-icon-location"></i>
           <span>子菜单</span>
          </template>
        </el-menu-item>
      </el-submenu>
    </el-menu>
    </el-aside>

      <el-main>
        <el-table :data="info.slice((currentPage-1)*pagesize,currentPage*pagesize)" >
          <el-table-column prop="dym" label="电影名" width="140">
          </el-table-column>
          <el-table-column prop="dy" label="导演" width="120">
          </el-table-column>
          <el-table-column prop="bj" label="编剧"> </el-table-column>
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
      </el-main>
    </el-container>
  </el-container>
</template>

<script>
export default {
  data() {
    return {
      currentPage: 1, // 初始页
      pagesize: 8, //    每页的数据
      totle: 0,
      info: []
    }
  },
  mounted() {
    this.$axios.get('/api/').then((response) => { this.info = response.data })
      .catch(function (error) { // 请求失败处理
        console.log(error);
      })
  },
  methods: {
    // 初始页currentPage、初始每页数据数pagesize和数据data
    handleSizeChange: function (size) {
      this.pagesize = size;
      nsole.log(this.pagesize) // 每页下拉显示数据
    },
    handleCurrentChange: function(currentPage) {
      this.currentPage = currentPage;
      console.log(this.currentPage) // 点击第几页
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
  .el-main {
    background-color: #eaedf1;
  }
</style>