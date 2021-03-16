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
                <el-button type="primary" icon="el-icon-edit" size="mini" @click="useredit(scope.row)"></el-button>
              </el-tooltip>
              <el-tooltip  effect="dark" content="删除" placement="top" :enterable="false">
                <el-button type="danger" icon="el-icon-delete" size="mini" @click="deleteuser(scope.row.id)" :disabled="isdeldisabled(scope.row.id)"></el-button>
              </el-tooltip>
              <el-tooltip  effect="dark" content="分配角色" placement="top" :enterable="false">
                <el-button type="warning" icon="el-icon-setting" size="mini" @click="assignrole(scope.row)"></el-button>
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
      <!--dialo修改新增用户弹出框 prop 是校验用的属性 -->
      <el-dialog :title="dialogform.title" :visible.sync="adddialogvisible" width="50%" @close="dialogclose">
        <el-form :model="dialogform"  :rules="dialogformrules" ref="dialogformref" label-width="70px">
           <!--隐藏id字段 -->
          <el-form-item label="id" v-show="false">
            <el-input v-model="dialogform.id"></el-input>
          </el-form-item>
          <el-form-item label="用户名" prop="username" >
            <el-input v-model="dialogform.username" autocomplete="off" :disabled="usernamedisabled"></el-input>
          </el-form-item>
          <el-form-item label="密码" prop="userpassword" >
            <el-input v-model="dialogform.userpassword" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="性别" width="30px" prop="usersex">
            <el-select v-model="dialogform.usersex" placeholder="选择性别" >
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
          <el-button type="primary" @click="userconfirm">确 定</el-button>
        </span>
      </el-dialog>
      <!--dialo分配角色弹出框 -->
      <el-dialog title="分配角色" :visible.sync="roledialogvisible" width="50%">
        <el-form :model="roledialogform" label-width="70px">
           <!--隐藏roleid字段 -->
          <el-form-item label="roleid" v-show="false">
            <el-input v-model="roledialogform.roleid"></el-input>
          </el-form-item>
           <!--隐藏userid字段 -->
          <el-form-item label="userid" v-show="false">
            <el-input v-model="roledialogform.userid"></el-input>
          </el-form-item>
          <el-form-item label="用户名" >
            <el-input v-model="roledialogform.username"  disabled></el-input>
          </el-form-item>
          <el-form-item label="原角色" >
            <el-input v-model="roledialogform.rolename" disabled></el-input>
          </el-form-item>
          <el-form-item label="新角色" width="30px" >
            <el-select v-model="value" placeholder="选择角色" >
              <el-option v-for="item in roleoptions"
              :key="item.roleid"
              :label="item.rolename"
              :value="item.roleid">
              </el-option>
            </el-select>
          </el-form-item>
        </el-form>
        <span slot="footer" class="dialog-footer">
          <el-button @click="roledialogvisible = false">取 消</el-button>
          <el-button type="primary" @click="roleconfirm">确 定</el-button>
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
      // 分配角色select框
      roleoptions: [],
      // 分配角色 select 框 绑定值
      value: '',
      // 添加用户弹出框可见
      adddialogvisible: false,
      // 分配角色弹出框可见
      roledialogvisible: false,
      // 修改时 用户名对话框 不可编辑
      usernamedisabled: false,
      // 添加用户对话框
      dialogform: {
        id: 0,
        username: '',
        userpassword: '',
        usersex: '',
        usereducation: '',
        userbirthday: '',
        title: '添加用户'
      },
      // 分配角色对话框
      roledialogform: {
        roleid: 0,
        userid: 0,
        username: '',
        rolename: ''
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
    // 判断如果数据行是登录用户，则不可删除自己
    isdeldisabled(id) {
      console.log(id + 'www')
      console.log(localStorage.getItem('userid') + 'www')
      if (localStorage.getItem('userid') == id) {
        return true
      }
      return false
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
    // 分配角色
    assignrole(row) {
      this.roledialogvisible = true
      this.roledialogform.username = row.username
      this.roledialogform.roleid = row.roleid
      this.roledialogform.userid = row.id
      this.$axios({
        method: 'get',
        url: '/api/role/'
      })
        .then((response) => {
          response.data.forEach(element => {
            this.roleoptions.push({ rolename: element.rolename, roleid: element.roleid })
          })
        })
        .catch(function (error) { // 请求失败处理
          console.log(error)
        })
        // 原角色名
        if (this.roledialogform.roleid != '') {
          this.$axios({
        method: 'get',
        url: '/api/role/' + this.roledialogform.roleid
      })
        .then((response) => {
          this.roledialogform.rolename = response.data.rolename
        })
        .catch(function (error) { // 请求失败处理
          console.log(error)
        })
        }
    },
    // 分配角色弹出框确定按钮
    roleconfirm() {
      this.$axios({
          method: 'put',
          url: '/api/user/' + this.roledialogform.userid,
          data: {
            roleid: this.value
          }
        })
          .then((response) => {
            if (response.status == 200) {
              this.$message.success('角色分配成功')
              // 成功后隐藏 分配角色弹出框
              this.roledialogvisible = false
              // 新增用户成功后刷新用户列表
              this.getlist()
            } else {
              this.$message.warning('角色分配失败')
            }
          })
          .catch(function (error) { // 请求失败处理
            console.log(error)
            this.$message.error('角色分配产生错误')
          })
    },
    // 关闭dialog 重置添加用户form
    dialogclose() {
      this.$refs.dialogformref.resetFields()
    },
    // 删除用户
    deleteuser(userid) {
      // 弹框询问是否删除
      this.$confirm('此操作将永久删除该用户, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        this.$axios({
          method: 'delete',
          url: '/api/user/' + userid
        })
          .then((response) => {
            if (response.status == 204) {
              this.$message.success('删除成功')
              // 刷新列表
              this.getlist()
            } else {
              this.$message.warning('删除失败')
            }
          })
          .catch(function (error) { // 请求失败处理
            console.log(error)
          })
      }).catch(() => {
        this.$message({
          type: 'info',
          message: '已取消删除'
        });
      });
    },
    // 弹出框 确定按钮 判断 新增用户还是修改用户 执行相应函数
    userconfirm() {
      console.log(this.dialogform.id)
      if (this.dialogform.title == '修改用户') {
        this.usereditput()
      } else {
        this.adduser()
      }
    },
    // select 下拉框 赋值后 强制刷新
    // 修改用户
    useredit(rowdata) {
      this.adddialogvisible = true
      this.usernamedisabled = true
      this.dialogform.title = '修改用户'
      this.dialogform.id = rowdata.id
      this.dialogform.username = rowdata.username
      this.dialogform.userpassword = rowdata.userpassword
      // v-model 绑定数据类型 string rowdata.usersex 是number 要转换一致
      this.dialogform.usersex = rowdata.usersex.toString()
      this.dialogform.userbirthday = rowdata.userbirthday
      this.dialogform.usereducation = rowdata.usereducation.toString()
    },
    // 修改用户提交
    usereditput() {
      // 进行校验
      this.$refs.dialogformref.validate(valid => {
        // 校验不通过 返回
        if (!valid) return
        // 校验通过 提交修改
        this.$axios({
          method: 'put',
          url: '/api/user/' + this.dialogform.id,
          data: {
            userpassword: this.dialogform.userpassword,
            usersex: this.dialogform.usersex,
            userbirthday: this.dialogform.userbirthday,
            usereducation: this.dialogform.usereducation
          }
        })
          .then((response) => {
            if (response.status == 200) {
              this.$message.success('修改用户成功')
              // 成功后隐藏 新增用户弹出框
              this.adddialogvisible = false
              // 新增用户成功后刷新用户列表
              this.getlist()
            } else {
              this.$message.warning('修改用户失败')
            }
          })
          .catch(function (error) { // 请求失败处理
            console.log(error)
            this.$message.error('修改用户产生错误')
          })
      })
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