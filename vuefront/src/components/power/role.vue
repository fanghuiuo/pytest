<template>
<div>
  <!-- 面包屑导航区域 -->
      <el-breadcrumb separator-class="el-icon-arrow-right">
        <el-breadcrumb-item :to="{ path: '/home' }">首页</el-breadcrumb-item>
        <el-breadcrumb-item>权限管理</el-breadcrumb-item>
        <el-breadcrumb-item>角色列表</el-breadcrumb-item>
      </el-breadcrumb>
       <!-- 卡片区域 -->
      <el-card class="box-card">
        <!-- 搜索框区域 -->
       <el-row :gutter="20">
        <el-col :span="6">
            <el-input placeholder="角色名"
            v-model="rolename" clearable>
            </el-input>
        </el-col>
        <el-col :span="6">
            <el-button type="primary" @click="getlist" >查询</el-button>
        </el-col>
         <el-col :span="6">
            <el-button type="primary" @click="adddialogvisible = true">添加角色</el-button>
        </el-col>

        </el-row>
        <!-- 表格区域 -->
        <el-table  :data="info.slice((currentPage-1)*pagesize,currentPage*pagesize)" border stripe>
           <el-table-column type="index"  label="序号" :index="table_index">
          </el-table-column>
          <el-table-column prop="rolename" label="角色名称" align="center">
          </el-table-column>
          <el-table-column prop="roledec" label="角色说明" align="center">
          </el-table-column>
          <el-table-column label="操作" align="center" width="200px">
            <template v-slot="scope">
              <el-tooltip  effect="dark" content="修改" placement="top" :enterable="false">
                <el-button type="primary" icon="el-icon-edit" size="mini" @click="roleedit(scope.row)"></el-button>
              </el-tooltip>
              <el-tooltip  effect="dark" content="删除" placement="top" :enterable="false">
                <el-button type="danger" icon="el-icon-delete" size="mini" @click="deleterole(scope.row.roleid)" ></el-button>
              </el-tooltip>
              <el-tooltip  effect="dark" content="分配权限" placement="top" :enterable="false">
                <el-button type="warning" icon="el-icon-setting" size="mini" @click="assignpermission(scope.row.roleid)"></el-button>
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
      <!--prop 是校验用的属性 -->
      <el-dialog :title="dialogform.title" :visible.sync="adddialogvisible" width="50%" @close="dialogclose">
        <el-form :model="dialogform"  :rules="dialogformrules" ref="dialogformref" label-width="70px">
          <!--隐藏id字段 -->
          <el-form-item label="roleid" v-show="false">
            <el-input v-model="dialogform.roleid"></el-input>
          </el-form-item>
          <el-form-item label="角色名称" prop="rolename" >
            <el-input v-model="dialogform.rolename" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="角色说明" prop="roledec" >
            <el-input v-model="dialogform.roledec" autocomplete="off"></el-input>
          </el-form-item>
        </el-form>
        <span slot="footer" class="dialog-footer">
          <el-button @click="adddialogvisible = false">取 消</el-button>
          <el-button type="primary" @click="roleconfirm">确 定</el-button>
        </span>
      </el-dialog>
       <!--分配权限对话框 -->
      <el-dialog title="分配权限" :visible.sync="pmdialogvisible" width="50%" @close="pmdialogclose">
        <!--方便使用roleid 隐藏 -->
        <el-input v-model="inputroleid" ></el-input>
        <!--树控件 -->
        <el-tree :data="treeinfo" :props="treeprops" show-checkbox node-key="id" default-expand-all
        :default-checked-keys="defkeys" ref="treeref"></el-tree>
        <span slot="footer" class="dialog-footer">
          <el-button @click="pmdialogvisible = false">取 消</el-button>
          <el-button type="primary" @click="assignconfirm">确 定</el-button>
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
      treeinfo: [],
      // 树默认选中的节点
      defkeys: [],
      rolename: '',
      // 添加角色弹出框可见
      adddialogvisible: false,
      // 分配权限对话框
      pmdialogvisible: false,
      // 角色id
      inputroleid: 0,
      // 修改时 角色名对话框 不可编辑
      rolenamedisabled: false,
      // 添加角色
      dialogform: {
        id: 0,
        rolename: '',
        roledec: '',
        title: '添加角色'
      },
      // 树绑定对象
      treeprops: {
        children: 'children',
        label: 'name'
      },
      dialogformrules: {
        rolename: [
          { required: true, message: '请输入角色名', trigger: 'blur' }
        ],
        roledec: [
          { required: true, message: '请输入角色说明', trigger: 'blur' }
        ]
      }
    }
  },
  methods: {
    // 得到角色列表
    getlist() {
      this.$axios({
        method: 'get',
        url: '/api/role/',
        params: {
          rolename: this.rolename
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
    // 保存 选定的权限
    assignconfirm() {
      // 数组转换为 字符串
      const keys = [
        // ...展开运算符,将一个数组转为用逗号分隔的参数序列 拿到全选和半选的 keys
        ...this.$refs.treeref.getCheckedKeys(),
        ...this.$refs.treeref.getHalfCheckedKeys()]
      if (keys != []) {
        const pmids = keys.join(',')
        console.log(keys)
        console.log(pmids)
        this.$axios({
          method: 'put',
          url: '/api/role/' + this.inputroleid,
          data: {
            pmids: pmids
          }
        })
          .then((response) => {
            if (response.status == 200) {
              this.$message.success('保存成功')
              // 成功后隐藏 分配权限弹出框
              this.pmdialogvisible = false
            } else {
              this.$message.warning('保存失败')
            }
          })
          .catch(function (error) { // 请求失败处理
            console.log(error)
            this.$message.error('产生错误')
          })
      }
    },
    // 分配权限
    assignpermission(roleid) {
      this.pmdialogvisible = true
      this.inputroleid = roleid
      this.$axios({
        method: 'get',
        url: '/api/permission/'
      }).then((response) => {
        // 将response.data 转换为数组
        const treelist = []
        for (const i in response.data) {
          treelist.push(response.data[i])
        }
        this.treeinfo = treelist
        this.getpermissiontree()
      })
      this.$axios({
        method: 'get',
        url: '/api/role/' + roleid
      }).then((response) => {
        // 已有权限打开选中,过滤只要第三级菜单 长度大于8 response.data.pmids.split(',') 是数组 再用filter过滤
        this.defkeys = response.data.pmids.split(',').filter(item => item.length > 8)
        console.log(response.data.pmids.split(','))
        console.log(this.defkeys)
      })
    },
    // 得到权限tree
    getpermissiontree() {
      const dataArray = []
      this.treeinfo.forEach(function (data) {
        const parentId = data.pm_pid
        if (parentId == 0) {
          const objTemp = {
            id: data.pmid,
            name: data.pmname,
            // order: data.order
            parentId: parentId
          }
          dataArray.push(objTemp)
        }
      })
      this.data2treeDG(this.treeinfo, dataArray)
    },
    data2treeDG(datas, dataArray) {
      for (let j = 0; j < dataArray.length; j++) {
        const dataArrayIndex = dataArray[j]
        const childrenArray = []
        const Id = dataArrayIndex.id
        for (let i = 0; i < datas.length; i++) {
          const data = datas[i]
          const parentId = data.pm_pid
          if (parentId == Id) { // 判断是否为儿子节点
            const objTemp = {
              id: data.pmid,
              name: data.pmname,
              /* order: data.order,*/
              parentId: parentId
            }
            childrenArray.push(objTemp)
          }
        }
        dataArrayIndex.children = childrenArray
        if (childrenArray.length > 0) { // 有儿子节点则递归
          this.data2treeDG(datas, childrenArray)
        }
      }
      this.treeinfo = dataArray
      return dataArray
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
    // 角色列表加序号字段
    table_index(index) {
      return (this.currentPage - 1) * this.pagesize + index + 1
    },
    // 关闭dialog 重置添加角色form
    dialogclose() {
      this.$refs.dialogformref.resetFields()
    },
    // 关闭分配权限dialog 重置 选中 数组 defkeys
    pmdialogclose() {
      this.defkeys = []
    },
    // 删除角色
    deleterole(roleid) {
      // 弹框询问是否删除
      this.$confirm('此操作将永久删除该角色, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        this.$axios({
          method: 'delete',
          url: '/api/role/' + roleid
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
    // 弹出框 确定按钮 判断 新增角色还是修改角色 执行相应函数
    roleconfirm() {
      console.log(this.dialogform.id)
      if (this.dialogform.title == '修改角色') {
        this.roleeditput()
      } else {
        this.addrole()
      }
    },
    // select 下拉框 赋值后 强制刷新
    // 修改角色
    roleedit(rowdata) {
      this.adddialogvisible = true
      this.rolenamedisabled = true
      this.dialogform.title = '修改角色'
      this.dialogform.id = rowdata.id
      this.dialogform.rolename = rowdata.rolename
      this.dialogform.roledec = rowdata.roledec
    },
    // 修改角色提交
    roleeditput() {
      // 进行校验
      this.$refs.dialogformref.validate(valid => {
        // 校验不通过 返回
        if (!valid) return
        // 校验通过 提交修改
        this.$axios({
          method: 'put',
          url: '/api/role/' + this.dialogform.roleid,
          data: {
            rolename: this.dialogform.rolename,
            roledec: this.dialogform.roledec
          }
        })
          .then((response) => {
            if (response.status == 200) {
              this.$message.success('修改角色成功')
              // 成功后隐藏 新增角色弹出框
              this.adddialogvisible = false
              // 新增角色成功后刷新角色列表
              this.getlist()
            } else {
              this.$message.warning('修改角色失败')
            }
          })
          .catch(function (error) { // 请求失败处理
            console.log(error)
            this.$message.error('修改角色产生错误')
          })
      })
    },
    // 添加角色
    addrole() {
      console.log(this.dialogform)
      this.$refs.dialogformref.validate(valid => {
        console.log(valid)
        // 校验不通过 返回
        if (!valid) return
        // 校验通过 先验证角色是否已存在
        this.$axios({
          method: 'get',
          url: '/api/role/',
          params: {
            rolename: this.dialogform.rolename
          }
        })
          .then((response) => {
            console.log(response.data.length)
            if (response.data.length !== 0) {
              // 角色存在 返回
              this.$message.warning('角色已存在 请更换角色名')
              this.dialogform.rolename = ''
            } else {
              // 角色不存在 post
              this.$axios({
                method: 'post',
                url: '/api/role/',
                data: {
                  rolename: this.dialogform.rolename,
                  roledec: this.dialogform.roledec
                }
              })
                .then((response) => {
                  console.log(response)
                  if (response.status == 201) {
                    this.$message.success('新增角色成功')
                    // 成功后隐藏 新增角色弹出框
                    this.adddialogvisible = false
                    // 新增角色成功后刷新角色列表
                    this.getlist()
                  } else {
                    this.$message.warning('新增角色失败')
                  }
                })
                .catch(function (error) { // 请求失败处理
                  console.log(error)
                  this.$message.error('新增角色产生错误')
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