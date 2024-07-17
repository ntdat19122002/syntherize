<template>
    <div class="content">
        <div class="shopify-api-method-list">
            <div class="shopify-api-method">
                <div class="shopify-api-method__header">
                    <button @click="postStoreFrontAccessScope()" class="post-shopify-api-button">Post</button>
                    <span class="shopify-api-method__header__title">Retrieves a list of storefront access tokens that have been issued</span>
                </div>
                <div class="shopify-api-method__result">
                    <div class="shopify-api-method__result_header">
                        Result
                    </div>
                    <div class="shopify-api-method__result_content">
                        {{ store_front_access_scope }}
                    </div>
                </div>
            </div>
            <GetAPIShopify
                title="Retrieves a list of storefront access tokens that have been issued"
                get_url="/store_front_access_token"
            />
        </div>
    </div>
</template>

<script>

import axios from "axios";
import GetAPIShopify from "../../../components/API/GetAPIShopify.vue";

export default {
    components: {GetAPIShopify},
    data() {
        return {
            store_front_access_scope: null
        }
    },
    methods: {
        postStoreFrontAccessScope() {
            axios.get('/create_store_front_access_token').then((res) => this.store_front_access_scope = res.data)
        }
    }
};
</script>

<style scoped>
</style>