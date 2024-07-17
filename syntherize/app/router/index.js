import {createRouter, createWebHistory} from 'vue-router'
import rest_api_paths from "./rest_api";
import royalty_app_paths from "./royalty_app";

const router = createRouter({
    history: createWebHistory(),
    routes: [
        ...rest_api_paths,
        ...royalty_app_paths
    ]
})

export default router
