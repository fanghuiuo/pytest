<template>
<div>
  <!-- 面包屑导航区域 -->
      <el-breadcrumb separator-class="el-icon-arrow-right">
        <el-breadcrumb-item :to="{ path: '/home' }">首页</el-breadcrumb-item>
        <el-breadcrumb-item>权限管理</el-breadcrumb-item>
        <el-breadcrumb-item>权限列表</el-breadcrumb-item>
      </el-breadcrumb>
       <!-- 卡片区域 -->
      <el-card class="box-card">
        <!-- 搜索框区域 -->
       <el-row :gutter="20">
        <el-col :span="6">
            <el-input placeholder="权限名"
            v-model="pmname" clearable>
            </el-input>
        </el-col>
        <el-col :span="6">
            <el-button type="primary" @click="getlist" >查询</el-button>
        </el-col>
        </el-row>
        <!-- 表格区域 -->
        <el-table  :data="info.slice((currentPage-1)*pagesize,currentPage*pagesize)" border stripe>
           <el-table-column type="index"  label="序号" :index="table_index">
          </el-table-column>
          <el-table-column prop="pmname" label="权限名称" align="center">
          </el-table-column>
          <el-table-column prop="pmurl" label="路径" align="center">
          </el-table-column>
          <el-table-column prop="pmlevel" label="权限等级" align="center">
             <template v-slot="scope">
              <el-tag v-if="scope.row.pmlevel == 0">一级</el-tag>
              <el-tag type="success" v-if="scope.row.pmlevel == 1">二级</el-tag>
              <el-tag type="warning" v-if="scope.row.pmlevel == 2">三级</el-tag>
            </template>
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
      pagesize: 5, //    每页默认的数据
      totle: 0,
      info: [],
      pmname: ''
    }
  },
  methods: {
    // 得到用户列表
    getlist() {
      this.$axios({
        method: 'get',
        url: '/api/permission/',
        params: {
          pmname: this.pmname
        }
      })
        .then((response) => {
          this.info = response.data
          console.log(response.data)
        })
        .catch(function (error) { // 请求失败处理
          console.log(error)
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
    // 用户列表加序号字段
    table_index(index) {
      return (this.currentPage - 1) * this.pagesize + index + 1
    }
  }
}
</script>

<style scoped>
</style>