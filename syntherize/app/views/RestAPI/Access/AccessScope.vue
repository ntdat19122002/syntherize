<template>
    <div class="content">
        <div class="shopify-api-method-list">
            <div class="shopify-api-method">
                <div class="shopify-api-method__header">
                    <button @click="getAccessScope()" class="get-shopify-api-button">Get</button>
                    <span class="shopify-api-method__header__title">Get a list of access scopes</span>
                </div>
                <div class="shopify-api-method__result">
                    <div class="shopify-api-method__result_header">
                        Result
                    </div>
                    <div class="shopify-api-method__result_content">
                        {{ access_scope }}
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>

import axios from "axios";

export default {
    data() {
        return {
            access_scope: null
        }
    },
    methods: {
        getAccessScope(){
            axios.get('/access_scope').then((res) => this.access_scope = res.data)
        }
    }
};
</script>

<style scoped>
</style>