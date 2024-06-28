<template>
  <Header/>
  <div class="wrapper">
    <Navbar/>
    <router-view/>
  </div>
</template>

<script>

import Navbar from "./components/Navbar.vue";
import Header from "./components/Header.vue";

export default {
  name: "App",
  components: {Header, Navbar},
  data() {
    return {};
  },
  methods: {
    test_method: function () {
      console.log('Test')
    }
  },
  computed: {},
  async mounted() {
  }
}
</script>
<style src="./css/variable.css"></style>
<style src="./css/main.css"></style>
<style>
.wrapper {
  display: flex;
  height: 91vh;
}
</style>