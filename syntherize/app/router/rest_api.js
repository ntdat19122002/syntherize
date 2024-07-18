import AccessScope from "../views/RestAPI/Access/AccessScope.vue";
import StorefrontAccessToken from "../views/RestAPI/Access/StorefrontAccessToken.vue";
import ApplicationCharge from "../views/RestAPI/Billing/ApplicationCharge.vue";
import ApplicationCredit from "../views/RestAPI/Billing/ApplicationCredit.vue";
import RecurringApplicationCharge from "../views/RestAPI/Billing/RecurringApplicationCharge.vue";
import UsageCharge from "../views/RestAPI/Billing/UsageCharge.vue";
import Webhook from "../views/RestAPI/Webhooks/Webhook.vue";

const rest_api_paths = [
    {
        path: '/apps/syntherize/restapi/access/access_scope',
        name: 'AccessScope',
        component: AccessScope
    },{
        path: '/apps/syntherize/restapi/access/store_front_access_scope',
        name: 'StorefrontAccessToken',
        component: StorefrontAccessToken
    },{
        path: '/apps/syntherize/restapi/billing/application_charge',
        name: 'ApplicationCharge',
        component: ApplicationCharge
    },{
        path: '/apps/syntherize/restapi/billing/application_credit',
        name: 'ApplicationCredit',
        component: ApplicationCredit
    },{
        path: '/apps/syntherize/restapi/billing/recurring_application_charge',
        name: 'RecurringApplicationCharge',
        component: RecurringApplicationCharge
    },{
        path: '/apps/syntherize/restapi/billing/usage_charge',
        name: 'UsageCharge',
        component: UsageCharge
    },{
        path: '/apps/syntherize/restapi/webhooks/webhook',
        name: 'Webhook',
        component: Webhook
    }
]

export default rest_api_paths