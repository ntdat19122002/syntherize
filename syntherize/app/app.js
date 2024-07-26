import {createApp, h} from 'vue/dist/vue.esm-bundler';
import router from './router'
import App from './App.vue'
import 'ant-design-vue/dist/antd.css';

window.localStorage.setItem('base_url', window.location.href)
import {createStore} from 'vuex'
import axios from "axios";

// Create a new store instance.
const store = createStore({
    state() {
        return {
            count: 0,
            ngrok_address: '',
        }
    },
    actions:{
        fetchData({commit}){
            axios.get('/vuex/default')
            .then(res => {
                commit('SET_DATA', res.data);
            })
        }
    },
    mutations: {
        increment(state) {
            state.count++
        },
        SET_DATA(state, payload) {
          state.ngrok_address = payload.ngrok_address;
        },
    }
})

var app = createApp({
    name: 'App',
    render: () => {
        return <App/>
    }
})

app.use(store)
app.use(router)

app.mount('#app-id')

