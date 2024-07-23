<template>
    <div class="shopify-api-method">
        <div class="shopify-api-method__result">
            <div class="shopify-api-method__result__header">
                <div class="shopify-api-method__result__header__title">
                    Result
                </div>
                <div @click="copyToClipboard" class="shopify-api-method__result__header__copy-to-clipboard">
                    📋
                </div>
            </div>
            <div class="shopify-api-method__result_content">
                {{ data }}
            </div>
        </div>
    </div>
</template>

<script>
export default {
    props:['data'],
    methods:{
        copyToClipboard(){
            navigator.clipboard.writeText(JSON.stringify(this.data));
        }
    }
};
</script>