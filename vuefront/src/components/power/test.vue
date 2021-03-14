<template>
  <div class="custom-tree-container">
    <el-tree
      :data="treeinfo"
      show-checkbox
      node-key="menuId"
      ref="tree"
      highlight-current
      :props="defaultProps"
    >
    </el-tree>
  </div>
</template>

<script>
export default {
  data() {
    return {
      treeinfo: [],
      defaultProps: {
        children: 'children',
        label: 'name'
      }
    }
  },
  methods: {
    getListData() {
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
        dataArrayIndex.children = childrenArray;
        console.log(666)
        console.log(dataArrayIndex.children)
        if (childrenArray.length > 0) { // 有儿子节点则递归
          this.data2treeDG(datas, childrenArray)
        }
      }
      this.treeinfo = dataArray
      return dataArray
    }
  },
  created() {
    // 这边是请求数据的
    this.$axios({
      method: 'get',
      url: '/api/permission/'
    }).then((response) => {
      const treelist = []
      for (const i in response.data) {
        treelist.push(response.data[i])
      }
      this.treeinfo = treelist
      console.log(treelist)
      this.getListData()
      // this.$router.push({ path: '/table' });
    })
  }
}
</script>
<style  scoped></style>
