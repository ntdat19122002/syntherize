<template>
  <div class="header">
    <div class="header-left">
      <div class="icon">Syntherize</div>
      <button>
        <span>upgrade</span>
      </button>
    </div>
    <div class="header-center">
      <div class="search">
        <i class="fa-solid fa-magnifying-glass"></i>
        <input type="text" placeholder="search customer name or email">
      </div>
    </div>
    <router-link :to="{name:'Profile'}" class="header-right" >
      ? TeststoreDat2
    </router-link>
  </div>
</template>

<script>

export default {

};
</script>

<style scoped>
  /* header */
  .header{
    padding: 5px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1px solid rgba(0,0,0,0.1);
  }

  .header .header-left{
    display: flex;
    align-items: center;
  }

  .header .header-left .icon{
    font-size: 32px;
  }

  .header .header-left button{
    height: 26px;
    border: none;
    margin-left: 5px;
    background: yellow;
    font-size: 12px;
    font-weight: 600;
    border-radius: 3px;
  }

  .header .header-center{
    width: 30%;
  }

  .header .header-center .search{
    display: flex;
    align-items: center;
    border:1px solid #c4cdd5;
  }

  .search i{
    padding: 5px;
  }

  .search input{
    width: 90%;
    border: none;
    padding: 5px 12px 5px 0;
  }
</style>