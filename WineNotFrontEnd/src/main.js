import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'
import axios from 'axios'
import './index.css'

axios.defaults.baseURL = 'http://localhost:8000' //url of python server

const app = createApp(App)

app.use(createPinia())
app.use(router, axios)

app.mount('#app')
