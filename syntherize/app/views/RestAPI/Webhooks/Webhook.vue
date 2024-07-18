<template>
    <div class="content">
        <div class="shopify-api-method-list">
            <GetAPIShopify
                title="Retrieves a list of webhooks"
                get_url="/webhook/list"
            />
        </div>
    </div>
</template>

<script>

import axios from "axios";
import GetAPIShopify from "../../../components/API/GetAPIShopify.vue";

export default {
    components: {GetAPIShopify}
};
</script>

<style scoped>
</style>