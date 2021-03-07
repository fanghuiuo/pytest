<template>
<div>
  <!-- 面包屑导航区域 -->
      <el-breadcrumb separator-class="el-icon-arrow-right">
        <el-breadcrumb-item :to="{ path: '/home' }">首页</el-breadcrumb-item>
        <el-breadcrumb-item>系统管理</el-breadcrumb-item>
        <el-breadcrumb-item>用户管理</el-breadcrumb-item>
      </el-breadcrumb>
       <!-- 卡片区域 -->
      <el-card class="box-card">
        <!-- 搜索框区域 -->
       <el-row :gutter="20">
        <el-col :span="6">
            <el-input placeholder="用户名"
            v-model="username" clearable>
            </el-input>
        </el-col>
        <el-col :span="6">
            <el-button type="primary" @click="getlist" >查询</el-button>
        </el-col>
         <el-col :span="6">
            <el-button type="primary" @click="adddialogvisible = true">添加用户</el-button>
        </el-col>

        </el-row>
        <!-- 表格区域 -->
        <el-table  :data="info.slice((currentPage-1)*pagesize,currentPage*pagesize)" border stripe>
           <el-table-column type="index"  label="序号" :index="table_index">
          </el-table-column>
          <el-table-column prop="username" label="姓名" align="center">
          </el-table-column>
          <el-table-column prop="usersex" label="性别" align="center">
            <template v-slot="scope">
              <!--判断等于1 则是男 否则是女 -->
              {{ scope.row.usersex === 1 ? '男' : '女' }}
            </template>
          </el-table-column>
          <el-table-column prop="userbirthday" label="生日" align="center">
          </el-table-column>
          <el-table-column prop="usereducation" label="学历" align="center">
            <template v-slot="scope">
              {{ scope.row.usereducation === 1 ? '高中' : scope.row.usereducation === 2 ? '本科' :scope.row.usereducation === 3 ? '硕士' : '博士'}}
            </template>
          </el-table-column>
          <el-table-column prop="is_active" label="状态" align="center">
             <template v-slot="scope">
              <el-switch v-model="scope.row.is_active"  @change="activechange(scope.row)">
              </el-switch>
            </template>
          </el-table-column>
          <el-table-column prop="createtime" label="创建时间" align="center">
          </el-table-column>
          <el-table-column prop="updatetime" label="修改时间" align="center">
          </el-table-column>
          <el-table-column label="操作" align="center" width="200px">
            <template v-slot="scope">
              <el-tooltip  effect="dark" content="修改" placement="top" :enterable="false">
                <el-button type="primary" icon="el-icon-edit" size="mini"></el-button>
              </el-tooltip>
              <el-tooltip  effect="dark" content="删除" placement="top" :enterable="false">
                <el-button type="danger" icon="el-icon-delete" size="mini"></el-button>
              </el-tooltip>
              <el-tooltip  effect="dark" content="分配角色" placement="top" :enterable="false">
                <el-button type="warning" icon="el-icon-setting" size="mini"></el-button>
              </el-tooltip>
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
      <el-dialog title="添加用户" :visible.sync="adddialogvisible" width="50%" @close="dialogclose">
        <el-form :model="dialogform"  :rules="dialogformrules" ref="dialogformref" label-width="70px">
          <el-form-item label="用户名" prop="username" >
            <el-input v-model="dialogform.username" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="密码" prop="userpassword" >
            <el-input v-model="dialogform.userpassword" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="性别" width="30px" prop="usersex">
            <el-select v-model="dialogform.usersex" placeholder="选择性别">
              <el-option label="男" value="1"></el-option>
              <el-option label="女" value="2"></el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="生日" prop="userbirthday" >
            <el-date-picker type="date" placeholder="选择日期" v-model="dialogform.userbirthday" format="yyyy 年 MM 月 dd 日" value-format="yyyy-MM-dd"></el-date-picker>
          </el-form-item>
          <el-form-item label="学历" width="30px" prop="usereducation">
            <el-select v-model="dialogform.usereducation" placeholder="选择学历">
              <el-option label="高中" value="1"></el-option>
              <el-option label="本科" value="2"></el-option>
              <el-option label="硕士" value="3"></el-option>
              <el-option label="博士" value="4"></el-option>
            </el-select>
          </el-form-item>
        </el-form>
        <span slot="footer" class="dialog-footer">
          <el-button @click="adddialogvisible = false">取 消</el-button>
          <el-button type="primary" @click="adduser">确 定</el-button>
        </span>
      </el-dialog>
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
      username: '',
      // 添加用户弹出框可见
      adddialogvisible: false,
      // 添加用户
      dialogform: {
        username: '',
        userpassword: '',
        usersex: '',
        usereducation: '',
        userbirthday: ''
      },
      dialogformrules: {
        username: [
          { required: true, message: '请输入用户名', trigger: 'blur' },
          { min: 1, max: 12, message: '长度在 1 到 12个字符', trigger: 'blur' }
        ],
        userpassword: [
          { required: true, message: '请输入密码', trigger: 'blur' },
          { min: 1, max: 12, message: '长度在 1 到 12个字符', trigger: 'blur' }
        ],
        usersex: [
          { required: true, message: '请选择性别', trigger: 'change' }
        ],
        // 把 校验 中的 type:date 去掉 防止报错
        userbirthday: [
          { required: true, message: '请选择日期', trigger: 'change' }
        ],
        usereducation: [
          { required: true, message: '请选择学历', trigger: 'change' }
        ]
      }
    }
  },
  methods: {
    // 得到用户列表
    getlist() {
      this.$axios({
        method: 'get',
        url: '/api/user/',
        params: {
          username: this.username
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
    },
    // 监听 状态按钮 改变用户状态
    activechange(rowdata) {
      console.log(rowdata)
      this.$axios({
        method: 'put',
        url: '/api/user/' + rowdata.id,
        data: {
          is_active: rowdata.is_active
        }
      })
        .then((response) => {
          console.log(response)
        })
        .catch(function (error) { // 请求失败处理
          console.log(error)
        })
    },
    // 关闭dialog 重置添加用户form
    dialogclose() {
      this.$refs.dialogformref.resetFields()
    },
    // 添加用户
    adduser() {
      console.log(this.dialogform)
      this.$refs.dialogformref.validate(valid => {
        console.log(valid)
        // 校验不通过 返回
        if (!valid) return
        // 校验通过 先验证用户是否已存在
        this.$axios({
          method: 'get',
          url: '/api/user/',
          params: {
            username: this.dialogform.username
          }
        })
          .then((response) => {
            console.log(response.data.length)
            if (response.data.length !== 0) {
              // 用户存在 返回
              this.$message.warning('用户已存在 请更换用户名')
              this.dialogform.username = ''
            } else {
              // 用户不存在 post
              this.$axios({
                method: 'post',
                url: '/api/user/',
                data: {
                  username: this.dialogform.username,
                  userpassword: this.dialogform.userpassword,
                  usersex: this.dialogform.usersex,
                  usereducation: this.dialogform.usereducation,
                  userbirthday: this.dialogform.userbirthday,
                  is_active: 0
                }
              })
                .then((response) => {
                  console.log(response)
                  if (response.status == 201) {
                    this.$message.success('新增用户成功')
                    // 成功后隐藏 新增用户弹出框
                    this.adddialogvisible = false
                    // 新增用户成功后刷新用户列表
                    this.getlist()
                  } else {
                    this.$message.warning('新增用户失败')
                  }
                })
                .catch(function (error) { // 请求失败处理
                  console.log(error)
                  this.$message.error('新增用户产生错误')
                })
            }
          })
          .catch(function (error) { // 请求失败处理
            console.log(error)
            this.$message.error('产生错误')
          })
      })
    }
  }
}
</script>

<style scoped>
</style>