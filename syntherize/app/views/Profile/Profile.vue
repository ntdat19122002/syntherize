<template>
  <div class="content">
      Ngrok address
      <input v-model="$store.ngrok_address" type="text"/>
  </div>
</template>

<script>

export default {
    data(){
        return{
        }
    },
    mounted(){
        console.log(this.$store.ngrok_address)
    }
};
</script>

<style scoped>
</style>