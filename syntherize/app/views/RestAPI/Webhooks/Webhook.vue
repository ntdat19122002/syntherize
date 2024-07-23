<template>
    <div class="content">
        <div class="shopify-api-method-list">
            <PostAPIShopify
                title="Create a new Webhook"
                url="/webhook"
                :body_data="{
                    webhook_address:null,
                    webhook_topic:null,
                    webhook_format:'json'
                }"
            />
            <GetAPIShopify
                title="Retrieves a list of webhooks"
                get_url="/webhook/list"
            />
            <GetAPIShopify
                title="Receive a single Webhook"
                get_url="/webhook"
                :body_data='{webhook_id:null}'
            />
            <GetAPIShopify
                title="Receive a count of all Webhooks"
                get_url="/webhook/count"
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
};
</script>

<style scoped>
</style>