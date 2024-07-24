<template>
    <div class="navbar">
        <select v-model="navbar_section">
            <option value="rest-api">Rest api</option>
            <option value="graphql-api">Graphql api</option>
            <option value="app">App</option>
        </select>
        <div v-if="navbar_section === 'rest-api'">
            <Menu :menu="rest_api_menu"/>
        </div>
        <div v-if="navbar_section === 'graphql-api'">
            <Menu :menu="graphql_menu"/>
        </div>
        <div v-else-if="navbar_section === 'app'">
            <Menu :menu="royalty_app_menu"/>
        </div>
    </div>
</template>

<script>
import menu from '../../config/menu.JSON'
import Menu from "./Menu.vue";
export default {
    components: {Menu},
    data(){
        return{
            navbar_section:"rest-api",
            rest_api_menu: menu.rest_api_menu,
            graphql_menu: menu.graphql_menu,
            royalty_app_menu: menu.royalty_menu
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