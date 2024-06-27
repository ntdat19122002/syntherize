<template>
  <div class="content points">
    <div class="content-head">
      <div class="title">Point</div> <div class="badge">Active</div>
    </div>

    <div class="content-item">
      <div class="left">
        <div class="title">Earn points</div>
        <div class="description">Create ways your customers can earn points when they join, share, and engage with your brand. Learn more about how customers earn points.</div>
        <button @click="showModalAddWayToEarn">Add ways to earn</button>
        <Modal v-model:visible="visibleModalAddWayToEarn" title="Basic Modal">
          <p>Some contents...</p>
          <p>Some contents...</p>
          <p>Some contents...</p>
        </Modal>
      </div>
      <div class="right">
        <div class="right-head">
          WAYS TO EARN
        </div>
      </div>
    </div>

    <div class="content-item">
      <div class="left">
        <div class="title">Earn points</div>
        <div class="description">Name your points currency to match your brand. We’ve put together a few tips for naming your points currency.</div>
      </div>
      <div class="right">
        <div class="right-head">
          Points currency
        </div>
        <div class="text-field">
          <label>Plural</label>
          <input type="text" placeholder="e.g. Points">
          <div class="description">An example message will look like this: You've earned 10 Points!</div>
        </div>
        <div class="text-field">
          <label>Singular</label>
          <input type="text" placeholder="e.g. Point">
          <div class="description">An example message will look like this: You've earned 1 Point!</div>
        </div>
        <button @click="saveNameOfPoint">Save</button>
      </div>
    </div>
  </div>
</template>

<script>
import {Modal} from 'ant-design-vue'
import axios from "axios";
export default {
  components: {Modal},
  data(){
    return{
      visibleModalAddWayToEarn:false
    }
  },
  methods:{
    showModalAddWayToEarn(){
      this.visibleModalAddWayToEarn = true
    },
    saveNameOfPoint(){
      axios.post('/point/name/save',{
        jsonrpc:2.0,
        params:{}
      })
    }
  }
};
</script>

<style scoped>
  .points{
    padding: 32px 10% 0;
  }

  .content-head{
    display: flex;
    align-items: center;
  }

  .content-head .title{
    font-size: 32px;
    font-weight: 600;
  }

  .content-head .badge{
    margin-left: 15px;
    font-size: 12px;
    padding: 2px 4px;
    background: #4dc44d;
    border-radius: 25px;
  }

  .content-item{
    display: flex;
    border-top: 1px solid rgba(0,0,0,0.1);
    margin-top: 15px;
    padding-top: 15px;
  }

  .content-item .left{
    width: 30%;
  }

  .content-item .left .title{
    font-size: 16px;
    font-weight: 600;
    margin: 15px 0;
  }

  .content-item .right{
    width: 70%;
  }
</style>