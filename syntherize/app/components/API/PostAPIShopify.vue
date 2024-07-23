<template>
    <div class="shopify-api-method">
        <div class="shopify-api-method__header">
            <button @click="getAccessScope()" class="post-shopify-api-button">Post</button>
            <span class="shopify-api-method__header__title">{{title}}</span>
        </div>
        <div v-if="body_data" class="shopify-api-method__input">
            <div v-for="(value, property) in body_data_temp">
                {{property}} <input  v-model="body_data_temp[property]" />
            </div>
        </div>
        <ResultAPIShopify :data="data"/>
    </div>
</template>

<script>

import axios from "axios";
import ResultAPIShopify from "./ResultAPIShopify.vue";

export default {
    components: {ResultAPIShopify},
    props:['title','url','body_data'],
    data() {
        return {
            data: null,
            body_data_temp:null
        }
    },
    methods: {
        getAccessScope(){
            axios.post(this.url,{
                jsonrpc:2.0,
                params:this.body_data_temp
            }).then((res) => {
                this.data = res.data
            })
        }
    },
    mounted() {
        this.body_data_temp = {...this.body_data}
    }
};
</script>