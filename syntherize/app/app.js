import {createApp, h} from 'vue/dist/vue.esm-bundler';
import router from './router'
import App from './App.vue'
import 'ant-design-vue/dist/antd.css';

window.localStorage.setItem('base_url',window.location.href)
var app = createApp({
    name: 'App',
    render: () => {
        return <App/>
    }
})

app.use(router)

app.mount('#app-id')

