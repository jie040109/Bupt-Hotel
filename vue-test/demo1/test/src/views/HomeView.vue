<template>
  <div id="app">
    <div class="container">
      <!-- Logo 和 Icon -->
      <div class="header">
        <img src="../assets/icon.png" alt="Icon" class="icon" />
      </div>

      <!-- HomeView 的内容 -->
      <div class="content">
        <h1>BUPT-Hotel</h1>
        <!-- 其余的 HomeView 内容 -->

        <div class="form-row">
          <label for="identity">选择身份:</label>
          <select id="identity" v-model="identity" @change="onIdentityChange">
            <option value="customer">Costumer</option>
            <option value="front_desk">Front Desk</option>
            <option value="administrator">Administrator</option>
          </select>
        </div>

        <div class="form-row" v-if="identity === 'customer'">
          <label for="account">Room_ID:</label>
          <input id="account" type="text" v-model="account">
        </div>

        <div class="form-row">
          <label for="password">Identity_card:</label>
          <input id="password" type="password" v-model="password">
        </div>

        <button @click="submit">登录</button>
      </div>

    </div>
  </div>
</template>

<script>
import { admin_login } from "@/admin";
import { user_login } from "@/user";
export default {
  data() {
    return {
      identity: 'customer',
      room: 'room1',
      account: '',
      password: ''
    };
  },
  methods: {
    onIdentityChange() {
      // 当身份更改时，可以在这里执行特定操作
    },
    submit() {
      // 如果身份是管理员，尝试登录
      if (this.identity === 'administrator') {
        admin_login(this.password)
          .then(() => {
            // 登录成功，跳转到控制室页面
            this.$router.push('/control-room');
          })
          .catch(error => {
            // 登录失败，处理错误
            console.error(error);
          });
      } else if (this.identity === 'customer') {
        user_login(this.account, this.password)
          .then(() => {
            // 登录成功，跳转到房间页面
            this.$router.push(`/room/${this.room}`);
          })
          .catch(error => {
            // 登录失败，处理错误
            console.error(error);
          });
        // 如果身份是客户，跳转到房间页面
        this.$router.push(`/room/${this.room}`);
      } else if (this.identity === 'front_desk') {
        // 如果身份是前台，跳转到前台页面
        this.$router.push('/front-desk');
      }
    }
  }
}
</script>

<style scoped>
/* 添加背景图 */

.container {
  background-image: url('../assets/2023.10.30.jpg');
  background-size: auto;
  background-position: center;
  background-attachment: scroll;
  min-height: 100vh;
  min-width: 95vw;
  /* 垂直堆叠子元素 */
  position: relative;
}

/* 样式调整为适应新布局 */
.header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  padding: 20px;
}

.icon {
  /* Icon 的样式 */
  width: 70px;
  /* 或者您期望的尺寸 */
}

.content {
  /* 适当调整内容区域的样式 */
  width: 50%;
  display: flex;
  flex-direction: column;
  /* 适当调整内容区域的样式 */
  max-width: 400px;

  margin: auto;
  padding: 20px;
  position: relative;

  background-color: rgba(255, 255, 255, 0.814);
  /* 可以提供一点透明度以显示背景 */
  gap: 40px;
  border-radius: 16px;
}

/* 设置输入框和下拉菜单的宽度和高度 */
/* 设置文本和密码输入框的共通样式 */
select {
  width: 80%;
  /* 或者您可以使用具体的像素值，例如：width: 300px; */
  height: 40px;
  /* 或根据您的设计要求调整 */
  padding: 10px;
  /* 文本内部的左右内边距 */
  margin-bottom: 10px;
  /* 控件之间的垂直间距 */
  box-sizing: border-box;
  /* 确保内边距和边框不会增加控件的宽度 */
  border: 1px solid #ccc;
  /* 控件边框样式 */
  border-radius: 4px;
  /* 控件边框圆角 */
}

.form-row {
  display: flex;
  align-items: center;
  justify-content: flex-start;
  margin-bottom: 10px;
}

.form-row label {
  white-space: nowrap;
  /* Ensure the label text stays on one line */
  margin-right: 10px;
}

.form-width {
  width: 250px;
  /* Set the width you want for your inputs and selects */
  padding: 10px;
  box-sizing: border-box;
  border: 1px solid #ccc;
  border-radius: 4px;
  margin-right: 10px;
}


input[type="text"],

input[type="password"],
select {
  width: 70%;
  /* 宽度充满容器 */
  height: 40px;
  /* 输入框的高度 */
  padding: 0px;
  /* 内边距，左右各10像素 */
  margin-bottom: 10px;
  /* 输入框之间的间隔 */
  box-sizing: border-box;
  /* 包括内边距和边框在内的总宽度 */
  border: 1px solid #ccc;
  /* 边框样式 */
  border-radius: 4px;
  /* 边框圆角 */
  font-size: 14px;
  /* 字体大小 */
  margin-left: auto
}

/* 如果需要，也可以为按钮设置样式 */
button {
  width: 100%;
  /* 按钮宽度与输入框相同 */
  height: 40px;
  /* 按钮高度 */
  padding: 10px;
  /* 按钮内边距 */
  margin-top: 0px;
  align-self: center;
  /* 与上方元素的间隔 */
  border: none;
  /* 无边框 */
  border-radius: 4px;
  /* 边框圆角 */
  background-color: #007bff;
  /* 背景颜色 */
  color: white;
  /* 字体颜色 */
  font-size: 16px;
  /* 字体大小 */
  cursor: pointer;
  /* 鼠标悬停时的光标样式 */
}

@media (max-width: 768px) {

  input[type="text"],
  input[type="password"],
  select,
  button {
    width: 100%;
  }
}

/* 其他样式 */
</style>