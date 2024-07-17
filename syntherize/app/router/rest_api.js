import AccessScope from "../views/RestAPI/Access/AccessScope.vue";
import StorefrontAccessToken from "../views/RestAPI/Access/StorefrontAccessToken.vue";

const rest_api_paths = [
    {
        path: '/apps/syntherize/restapi/access/access_scope',
        name: 'AccessScope',
        component: AccessScope
    },{
        path: '/apps/syntherize/restapi/access/store_front_access_scope',
        name: 'StorefrontAccessToken',
        component: StorefrontAccessToken
    },
]

export default rest_api_paths