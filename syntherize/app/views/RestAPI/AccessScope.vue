<template>
  <div class="content">
    Access scope
  </div>
</template>

<script>

import axios from "axios";

export default {
    data(){
      return{
          access_scope:null
      }
    },
    mounted() {
        axios.get('/access_scope').then(()=>console.log(1))
    }
};
</script>

<style scoped>
</style>