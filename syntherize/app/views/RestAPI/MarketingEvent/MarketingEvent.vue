<template>
    <div class="content">
        <div class="shopify-api-method-list">
            <GetAPIShopify
                title="Get a list of access scopes"
                get_url="/access_scope"
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