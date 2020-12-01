<template>
  <div class="login_container">
    <div class="login_box">
      <!-- Avatar -->
      <div class="avatar_box">
        <img src="../assets/yhl_lr.png" />
      </div>
      <!-- Login Form -->
      <el-form
        ref="loginFormRef"
        :model="form"
        :rules="loginFormRules"
        class="login_form"
        label-width="0px"
      >
        <!-- Login Items -->
        <el-form-item prop="username" label="Username">
          <el-input
            v-model="form.username"
            prefix-icon="el-icon-user"
          ></el-input>
        </el-form-item>
        <el-form-item prop="password" label="Password">
          <el-input
            v-model="form.password"
            prefix-icon="el-icon-lock"
            type="password"
          ></el-input>
        </el-form-item>

        <!-- Buttons -->
        <el-form-item class="btns">
          <el-button @click="login" type="primary">登陆</el-button>
          <el-button @click="resetFormData" type="info">重置</el-button>
        </el-form-item>
      </el-form>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      form: {
        username: "drop",
        password: "TQcps123",
      },
      loginFormRules: {
        username: [
          {
            required: true,
            message: "Please input your username...",
            trigger: "blur",
          },
          { min: 3, max: 10, message: "username.length must in [3, 10]" },
        ],
        password: [
          {
            required: true,
            message: "Please input password...",
            trigger: "blur",
          },
          { min: 6, max: 15, message: "username.length must in [6, 15]" },
        ],
      },
    };
  },
  methods: {
    resetFormData() {
      this.$refs.loginFormRef.resetFields();
    },
    login() {
      this.$refs.loginFormRef.validate(async (valid) => {
        if (!valid) return;
        // const { data: res } = await this.$http.get("drop");
        const { data: res } = await this.$http.post("login", this.form);
        if (res.meta.status!=200) {
            this.$message.error(res.meta.message)
        } else {
            this.$message.success(res.meta.message)
            window.sessionStorage.setItem('token', res.data.token)
            this.$router.push('/home')
        }
      });
    },
  },
};
</script>

<style lang="less" scoped>
.login_container {
  height: 100%;
  background-color: #2b4b6b;
}
.login_box {
  width: 450px;
  height: 300px;
  background-color: #ffffff;
  border-radius: 3px;
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);

  .avatar_box {
    height: 130px;
    width: 130px;
    border: 1px solid #eeeeee;
    border-radius: 50%;
    padding: 10px;
    box-shadow: 0 0 10px #dddddd;
    position: absolute;
    left: 50%;
    transform: translate(-50%, -50%);
    background-color: #ffffff;
    img {
      width: 100%;
      height: 100%;
      border-radius: 50%;
      background-color: #eeeeee;
    }
  }

  .btns {
    display: flex;
    justify-content: flex-end;
  }

  .login_form {
    position: absolute;
    bottom: 0;
    width: 100%;
    padding: 0 20px;
    box-sizing: border-box;
  }
}
</style>
