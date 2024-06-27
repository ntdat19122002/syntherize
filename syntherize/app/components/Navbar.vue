<template>
    <div class="navbar">
        <select v-model="navbar_section">
            <option value="rest-api">Rest api</option>
            <option value="graphql-api">Graphql api</option>
            <option value="app">App</option>
        </select>
        <div v-if="navbar_section === 'rest-api'">
            <div v-for="menu_item in rest_api_menu">
                <div class="navbar-item">
                    <router-link :to="{name:menu_item}">{{ menu_item }}</router-link>
                </div>
            </div>
        </div>
        <div v-if="navbar_section === 'graphql-api'">
            graph api
        </div>
        <div v-else-if="navbar_section === 'app'">
            <div class="navbar-item">
                <router-link :to="{name:'Dashboard'}">Home</router-link>
            </div>
            <div class="navbar-item">
                <div>Program</div>
                <div class="sub-navbar-item">
                    <router-link :to="{name:'Points'}">Points</router-link>
                </div>
                <div class="sub-navbar-item">
                    <router-link :to="{name:'Referrals'}">Referrals</router-link>
                </div>
                <div class="sub-navbar-item">
                    <router-link :to="{name:'Vip'}">Vip</router-link>
                </div>
                <div class="sub-navbar-item">
                    <router-link :to="{name:'Activity'}">Activity</router-link>
                </div>
            </div>
            <div class="navbar-item">
                <router-link :to="{name:'Customers'}">Customers</router-link>
            </div>
            <div class="navbar-item">
                <router-link :to="{name:'Performance'}">Performance</router-link>
            </div>
            <div class="navbar-item">
                <router-link :to="{name:'Branding'}">Branding</router-link>
            </div>
            <div class="navbar-item">
                <router-link :to="{name:'CustomerEmail'}">Customer email</router-link>
            </div>
            <div class="navbar-item">
                <router-link :to="{name:'Nudges'}">Nudges</router-link>
            </div>
            <div class="navbar-item">
                <router-link :to="{name:'Billing'}">Billing</router-link>
            </div>
        </div>
    </div>
</template>

<script>

export default {
    data(){
        return{
            navbar_section:'rest-api',
            rest_api_menu:['AccessScope']
        }
    }
};
</script>

<style scoped>
select{
    width: 100%;
}
.navbar {
    width: 240px;
    padding: 20px 10px;
    border-right: 1px solid rgba(0, 0, 0, 0.1);
}

.sub-navbar-item {
    margin-left: 20px;
}
</style>