<template>
    <div class="content">
        <h2>Explorer</h2>
        <textarea v-model="input"></textarea>
        <button @click="fetchGraphql">Fetch</button>
        <div>{{output}}</div>
    </div>
</template>

<script>

import axios from "axios";

export default {
    data(){
        return{
            input:'',
            output:''
        }
    },
    methods:{
        fetchGraphql(){
            axios.post('/graphql/explorer',{
                jsonrpc:2.0,
                params:{
                    explorer_input: this.input
                }
            }).then(res => {
                this.output = res.data
            })
        }
    }
};
</script>

<style scoped>
textarea{
    width: 100%;
    min-height: 150px;
}
</style>