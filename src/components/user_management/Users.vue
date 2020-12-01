<template>
  <div>
    <!-- Breadcrumb Nav -->
    <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item>首页</el-breadcrumb-item>
      <el-breadcrumb-item>用户管理</el-breadcrumb-item>
      <el-breadcrumb-item>用户列表</el-breadcrumb-item>
    </el-breadcrumb>

    <!-- In Card: Search -->
    <el-card>
      <el-row :gutter="18">
        <el-col :span="8">
          <el-input
            placeholder="请输入内容"
            v-model="queryInfo.query"
            clearable
            @clear="getUserList"
          >
            <el-button
              slot="append"
              icon="el-icon-search"
              @click="getUserList"
            ></el-button>
          </el-input>
        </el-col>
        <el-col :span="4">
          <el-button type="primary" @click="addDialogVisible = true"
            >添加用户</el-button
          >
        </el-col>
      </el-row>

      <!-- In Card: Table -->
      <el-table :data="userList" border stripe>
        <el-table-column type="index" label="#"></el-table-column>
        <el-table-column label="姓名" prop="username"></el-table-column>
        <el-table-column label="邮箱" prop="email"></el-table-column>
        <el-table-column label="电话" prop="mobile"></el-table-column>
        <el-table-column label="公司" prop="company"></el-table-column>
        <el-table-column label="位置" prop="position"></el-table-column>
        <!-- <el-table-column label="角色" prop="role_name"></el-table-column> -->
        <!-- <el-table-column label="状态" prop="mg_state">
        <template slot-scope="scope">
          <el-switch
            v-model="scope.row.mg_state"
            @change="userStateChange(scope.row.mg_state)"
          ></el-switch>
        </template>
      </el-table-column> -->
        <el-table-column label="操作" width="185px">
          <template slot-scope="scope">
            <el-button
              @click="showEditDialog(scope.row.id)"
              type="primary"
              icon="el-icon-edit"
              size="mini"
              >修改</el-button
            >
            <el-button
              @click="showDeleteDialog(scope.row.id)"
              type="danger"
              icon="el-icon-delete"
              size="mini"
              >删除</el-button
            >
          </template>
        </el-table-column>
      </el-table>
      <!-- Pagenation -->
      <el-pagination
        @size-change="handleSizeChange"
        @current-change="handleCurrentChange"
        :current-page="queryInfo.pageNum"
        :page-sizes="[1, 2, 5, 10]"
        :page-size="queryInfo.pageSize"
        layout="total, sizes, prev, pager, next, jumper"
        :total="total"
      >
      </el-pagination>
    </el-card>

    <!-- Dialog UserInfo -->
    <el-dialog
      title="添加用户"
      :visible.sync="addDialogVisible"
      width="50%"
      @close="addUserDialogClose"
    >
      <!-- Add User Form -->
      <el-form
        :model="addUserForm"
        :rules="addUserFormRules"
        ref="addUserFormRef"
        label-width="70px"
      >
        <el-form-item label="用户名" prop="username">
          <el-input v-model="addUserForm.username"></el-input> </el-form-item
        ><el-form-item label="公司" prop="company">
          <el-input v-model="addUserForm.company"></el-input>
        </el-form-item>
        <el-form-item label="地址" prop="position">
          <el-input v-model="addUserForm.position"></el-input>
        </el-form-item>
        <el-form-item label="手机" prop="mobile">
          <el-input v-model="addUserForm.mobile"></el-input>
        </el-form-item>
        <el-form-item label="邮箱" prop="email">
          <el-input v-model="addUserForm.email"></el-input> </el-form-item
      ></el-form>
      <span slot="footer" class="dialog-footer">
        <el-button @click="addDialogVisible = false">取 消</el-button>
        <el-button type="primary" @click="addUser">确 定</el-button>
      </span>
    </el-dialog>

    <!-- Dialog UserEdit -->
    <el-dialog
      title="修改用户"
      :visible.sync="editDialogVisible"
      width="50%"
      @close="editUserDialogClose"
    >
      <!-- Edit User Form -->
      <el-form
        :model="editUserForm"
        :rules="editUserFormRules"
        ref="editUserFormRef"
        label-width="70px"
      >
        <el-form-item label="公司" prop="company">
          <el-input v-model="editUserForm.company"></el-input>
        </el-form-item>
        <el-form-item label="地址" prop="position">
          <el-input v-model="editUserForm.position"></el-input>
        </el-form-item>
        <el-form-item label="手机" prop="mobile">
          <el-input v-model="editUserForm.mobile"></el-input>
        </el-form-item>
        <el-form-item label="邮箱" prop="email">
          <el-input v-model="editUserForm.email"></el-input> </el-form-item
      ></el-form>
      <span slot="footer" class="dialog-footer">
        <el-button @click="editDialogVisible = false">取 消</el-button>
        <el-button type="primary" @click="editUserInfo">确 定</el-button>
      </span>
    </el-dialog>

    <!-- Dialog UserDelete -->
    <el-dialog
      title="删除用户"
      :visible.sync="deleteDialogVisible"
      width="50%"
      @close="deleteUserDialogClose"
    >
      <span>确认删除该用户吗？</span>
      <span slot="footer" class="dialog-footer">
        <el-button @click="deleteDialogVisible = false">取 消</el-button>
        <el-button type="primary" @click="deleteUser">确 定</el-button>
      </span>
    </el-dialog>
  </div>
</template>

<script>
export default {
  data() {
    // var checkMobile = (rule, value, cb) => {
    //   const regMobile = /^(0|86|17951)?(13[0-9]|15[012356789]|17[678]|18[0-9]|14[5-7])[0-9]{8}$/;
    //   if (regMobile.test(value)) {
    //     return cb();
    //   }
    //   cb(new Error("Please input a real phone-number"));
    // };

    return {
      queryInfo: {
        query: "",
        pageNum: 1,
        pageSize: 5,
      },
      userList: [],
      total: 0,
      addDialogVisible: false,
      editDialogVisible: false,
      deleteDialogVisible: false,
      addUserForm: {
        username: "",
        email: "",
        mobile: "",
        company: "",
        position: "",
      },
      editUserForm: {
        email: "",
        mobile: "",
        company: "",
        position: "",
      },
      deletUserID: 0,
      addUserFormRules: {
        username: [
          {
            required: true,
            message: "Please input username of a new user",
            trigger: "blur",
          },
          {
            min: 3,
            max: 10,
            message: "username.length must in [3, 10]",
            trigger: "blur",
          },
        ],
        company: [
          {
            required: true,
            message: "Please input company-name of a new user",
            trigger: "blur",
          },
        ],
        position: [
          {
            required: true,
            message: "Please input location of a new user",
            trigger: "blur",
          },
        ],
        mobile: [
          {
            required: true,
            message: "Please input mobile of a new user",
            trigger: "blur",
          },
          //   {
          //     validator: checkMobile,
          //     trigger: "blur",
          //   },
        ],
        email: [
          {
            required: true,
            message: "Please input email of a new user",
            trigger: "blur",
          },
          //   {
          //     type: "email",
          //     message: "Please input a real email-address",
          //     trigger: ["blur", "change"],
          //   },
        ],
      },
      editUserFormRules: {},
    };
  },
  created() {
    this.getUserList();
  },
  methods: {
    async getUserList() {
      const { data: res } = await this.$http.get("users", {
        params: this.queryInfo,
      });
      if (res.meta.status !== 200) return this.$message.error(res.meta.message);
      this.$message.success(res.meta.message);
      this.userList = res.data.users;
      this.total = res.data.total;
    },
    handleSizeChange(newSize) {
      this.queryInfo.pageSize = newSize;
      this.getUserList();
    },
    handleCurrentChange(newPageNum) {
      this.queryInfo.pageNum = newPageNum;
      this.getUserList();
    },
    async userStateChange(userinfo) {
      console.log(userinfo);
      const { data: res } = await this.$http.put(
        `users/${userinfo.id}/state/${userinfo.mg_state}`
      );
      if (res.meta.status !== 200) return this.$message.error(res.meta.message);
      this.$message.success(res.meta.message);
    },
    addUserDialogClose() {
      this.$refs.addUserFormRef.resetFields();
    },
    editUserDialogClose() {
      this.$refs.editUserFormRef.resetFields();
    },
    deleteUserDialogClose() {
      this.deletUserID = 0;
    },
    addUser() {
      this.$refs.addUserFormRef.validate(async (valid) => {
        if (!valid) return this.$message.warning("form data not valid");
        const { data: res } = await this.$http.post("users", this.addUserForm);
        if (res.meta.status !== 201)
          return this.$message.error(res.meta.message);
        this.$message.success(res.meta.message);
        this.addDialogVisible = false;
        this.getUserList();
      });
    },
    async editUserInfo() {
      // post_data = this.editUserForm
      // post_data.action = 'change'
      const { data: res } = await this.$http.post("users/", this.editUserForm);
      if (res.meta.status !== 200) return this.$message.error(res.meta.message);
      console.log(res.meta.message);
      this.editDialogVisible = false;
      this.getUserList();
    },
    async deleteUser() {
      const { data: res } = await this.$http.get("users/", {
        params: { id: this.deletUserID, action: "delete" },
      });
      if (res.meta.status !== 200) return this.$message.error(res.meta.message);
      console.log(res.meta.message);
      this.deleteDialogVisible = false;
      this.getUserList();
    },
    async showEditDialog(userID) {
      console.log(userID);
      const { data: res } = await this.$http.get("users/", {
        params: { id: userID },
      });

      if (res.meta.status !== 200) return this.$message.error(res.meta.message);
      this.editUserForm = res.data;
      this.editDialogVisible = true;
    },
    showDeleteDialog(userID) {
      this.deleteDialogVisible = true;
      this.deletUserID = userID;
    },
  },
};
</script>

<style lang="less" scoped></style>
