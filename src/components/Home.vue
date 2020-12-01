<template>
  <el-container class="home-container">
    <el-header
      ><div>
        <img src="../assets/yhl_lr.png" width="50px" height="50px" />
        <span>水知行CMS后台</span>
      </div>
      <el-button @click="logout" type="info">登出</el-button></el-header
    >
    <el-container>
      <!-- SideNav -->
      <el-aside :width="isCollaps ? '64px' : '200px'"
        ><div @click="toggleCollaps" class="toggle-button">|||</div>
        <el-menu
          class="el-menu-vertical-demo"
          background-color="#333744"
          text-color="#fff"
          active-text-color="#409eff"
          unique-opened
          :collapse="isCollaps"
          :collapse-transition="false"
          router
          :default-active="activePath"
        >
          <!-- Level 1 -->
          <el-submenu
            v-for="item in menuList"
            :key="item.id"
            :index="item.id + ''"
          >
            <template slot="title">
              <i class="el-icon-location"></i>
              <span>{{ item.authName }}</span>
            </template>
            <!-- Level 2 -->
            <el-menu-item
              v-for="subItem in item.children"
              :key="subItem.id+''"
              :index="subItem.path"
              @click="saveNavState(subItem.path)"
            >
              <i class="el-icon-menu"></i>
              <span>{{ subItem.authName }}</span>
            </el-menu-item>
          </el-submenu>
        </el-menu></el-aside
      >
      <el-main>
          <router-view></router-view>
      </el-main>
    </el-container>
  </el-container>
</template>
<script>
export default {
  data() {
    return {
      menuList: [],
      isCollaps: false,
      activePath: ''
    };
  },
  methods: {
    logout() {
      window.sessionStorage.clear();
      this.$router.push("/login");
    },
    async getMenuList() {
      const { data: res } = await this.$http.get("menus");
      if (res.meta.status !== 200) return this.$message.error(res.meta.message);
      this.$message.success(res.meta.message);
      this.menuList = res.data;
    },
    pushPath(path) {
        this.$router.push(path)
    },
    toggleCollaps() {
        this.isCollaps = !this.isCollaps
    },
    saveNavState(activePath){
        window.sessionStorage.setItem('activePath', activePath)
    }
  },
  created() {
    this.getMenuList();
    this.activePath = window.sessionStorage.getItem('activePath')
  },
};
</script>
<style lang="less" scoped>
.el-header {
  background-color: #373d41;
  display: flex;
  justify-content: space-between;
  padding-left: 0;
  align-items: center;
  color: #ffffff;
  font-size: 20px;
  > div {
    display: flex;
    align-items: center;

    span {
      margin-left: 15px;
    }
  }
}

.el-aside {
  background-color: #333744;
  .el-menu {
      border-right: none;
  }
}

.el-main {
  background-color: #eaedf1;
}

.home-container {
  height: 100%;
}

.toggle-button {
    background-color: #4a5064;
    font-size: 10px;
    line-height: 24px;
    color: #ffffff;
    text-align: center;
    letter-spacing: 0.3em;
    cursor: pointer;
}
</style>
