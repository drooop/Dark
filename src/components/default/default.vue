<template>
  <div>
    <el-button @click="getUserListFromYHL">GetData</el-button>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {};
  },
  methods: {
    async getUserListFromYHL() {
      const drop_http = axios.create({
        timeout: 5000,
        async: true,
        crossDomain: true,
        headers: { "Content-type": "application/x-www-form-urlencoded" },
      });
      
      const {data: res} = await drop_http.get('http://10.30.0.3:8803/help');

      console.log(res)
    },
  },
};
</script>
<style></style>
