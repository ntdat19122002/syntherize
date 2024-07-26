<template>
    <div class="shopify-api-method">
        <div class="shopify-api-method__header">
            <button @click="getAccessScope()" class="del-shopify-api-button">Del</button>
            <span class="shopify-api-method__header__title">{{ title }}</span>
        </div>
        <div v-if="body_data && body_data_temp" class="shopify-api-method__input">
            <div v-for="(property_value, property) in body_data">
                <div v-if="Array.isArray(property_value) ">
                    {{ property }}
                    <Select
                        v-model:value="body_data_temp[property]"
                        show-search
                        style="width: 100%"
                        placeholder="Please select"
                        :options="formatOptions(property_value)"
                    ></Select>
                </div>
                <div v-else>
                    {{ property }} <input v-model="body_data_temp[property]"/>
                </div>
            </div>
        </div>
        <ResultAPIShopify :data="data"/>
    </div>
</template>

<script>
import {Select} from 'ant-design-vue'
import axios from "axios";
import ResultAPIShopify from "./ResultAPIShopify.vue";

export default {
    components: {ResultAPIShopify,Select},
    props: ['title', 'url', 'body_data'],
    data() {
        return {
            data: null,
            body_data_temp: null
        }
    },
    methods: {
        getAccessScope() {
            axios.post(this.url, {
                jsonrpc: 2.0,
                params: this.body_data_temp
            }).then((res) => {
                this.data = res.data
            })
        },
        formatOptions(value){
            return value.map((option) => ({
                label: option,
                value: option
            }))
        }
    },
    computed:{

    },
    mounted() {
        this.body_data_temp = {...this.body_data}
        for (let [key,value] of Object.entries(this.body_data_temp)){
            if(Array.isArray(value)){
                this.body_data_temp[key] = ''
            }
        }
    }
};
</script>
