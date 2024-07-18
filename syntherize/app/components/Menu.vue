<template>
    <div v-for="menu_item in menu">
        <div class="navbar-item" v-if="typeof (menu_item) != 'object'">
            <router-link :to="{name:menu_item}">{{ menu_item }}</router-link>
        </div>
        <div v-else>
            <div v-for="(sub_nav_bar_item_list,navbar_item_name) in menu_item">
                <div class="navbar-item">{{navbar_item_name}}</div>
                <div class="sub-navbar-item" v-for="sub_nav_bar_item in sub_nav_bar_item_list">
                    <router-link :to="{name:sub_nav_bar_item}">{{ sub_nav_bar_item }}</router-link>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    props:['menu']
};
</script>

<style scoped>

.sub-navbar-item {
    margin-left: 20px;
}
</style>