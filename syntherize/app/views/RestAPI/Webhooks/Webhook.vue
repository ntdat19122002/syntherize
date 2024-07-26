<template>
    <div class="content">
        <div class="shopify-api-method-list">
            <PostAPIShopify
                title="Create a new Webhook"
                url="/webhook"
                :body_data="{
                    webhook_address:$store.ngrok_address,
                    webhook_topic:webhook_list,
                    webhook_format:'json'
                }"
            />
            <GetAPIShopify
                title="Retrieves a list of webhooks"
                url="/webhook/list"
            />
            <GetAPIShopify
                title="Receive a single Webhook"
                url="/webhook"
                :body_data='{webhook_id:null}'
            />
            <GetAPIShopify
                title="Receive a count of all Webhooks"
                url="/webhook/count"
            />
            <PutAPIShopify
                title="Modify an existing Webhook"
                url="/webhook/upgrade"
                :body_data="{
                    webhook_id:null,
                    webhook_topic:webhook_list,
                    webhook_address:$store.ngrok_address+'webhook',
                }"
            />
            <DelAPIShopify
                title="Remove an existing Webhook"
                url="/webhook/delete"
                :body_data="{
                    webhook_id:null,
                    webhook_topic:webhook_list,
                }"
            />
        </div>
        <div class="webhook-data-list">

        </div>
    </div>
</template>

<script>

import axios from "axios";
import GetAPIShopify from "../../../components/API/GetAPIShopify.vue";
import PostAPIShopify from "../../../components/API/PostAPIShopify.vue";
import PutAPIShopify from "../../../components/API/PutAPIShopify.vue";
import webhook_list from "../../../../config/webhook.JSON"
import DelAPIShopify from "../../../components/API/DelAPIShopify.vue";
export default {
    components: {DelAPIShopify, PostAPIShopify, GetAPIShopify,PutAPIShopify},
    data(){
        return{
            webhook_list: webhook_list
        }
    }
};
</script>

<style scoped>
</style>