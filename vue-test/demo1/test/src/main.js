//创建者：王俊杰  

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
// import ElementPlus from 'element-plus'
// import 'element-plus/dist/index.css'

// createApp(App).use(ElementPlus)
createApp(App).use(store).use(router).mount('#app')
