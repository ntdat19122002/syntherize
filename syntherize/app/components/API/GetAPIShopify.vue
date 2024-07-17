<template>
    <div class="shopify-api-method">
        <div class="shopify-api-method__header">
            <button @click="getAccessScope()" class="get-shopify-api-button">Get</button>
            <span class="shopify-api-method__header__title">{{title}}</span>
        </div>
        <div class="shopify-api-method__result">
            <div class="shopify-api-method__result_header">
                Result
            </div>
            <div class="shopify-api-method__result_content">
                {{ data }}
            </div>
        </div>
    </div>
</template>

<script>

import axios from "axios";

export default {
    props:['title','get_url'],
    data() {
        return {
            data: null
        }
    },
    methods: {
        getAccessScope(){
            axios.get(this.get_url).then((res) => this.data = res.data)
        }
    }
};
</script>