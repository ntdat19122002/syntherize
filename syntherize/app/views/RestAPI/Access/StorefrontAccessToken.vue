<template>
    <div class="content">
        <div class="shopify-api-method-list">
            <PostAPIShopify
                title="Creates a new StorefrontAccessToken"
                url="/store_front_access_token"
            />
            <GetAPIShopify
                title="Retrieves a list of storefront access tokens that have been issued"
                url="/store_front_access_token"
            />
        </div>
    </div>
</template>

<script>

import axios from "axios";
import GetAPIShopify from "../../../components/API/GetAPIShopify.vue";
import PostAPIShopify from "../../../components/API/PostAPIShopify.vue";

export default {
    components: {PostAPIShopify, GetAPIShopify},
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