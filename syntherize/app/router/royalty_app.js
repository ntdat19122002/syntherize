import Dashboard from "../views/Dashboard.vue";
import Activity from "../views/Program/Activity.vue";
import Points from "../views/Program/Points.vue";
import Referrals from "../views/Program/Referrals.vue";
import Vip from "../views/Program/Vip.vue";
import Customers from "../views/Apps/Royalty/Customers.vue";
import Performance from "../views/Apps/Royalty/Performance.vue";
import Branding from "../views/Apps/Royalty/Branding.vue";
import CustomerEmail from "../views/Apps/Royalty/CustomerEmail.vue";
import Nudges from "../views/Apps/Royalty/Nudges.vue";
import Billing from "../views/Apps/Royalty/Billing.vue";

const paths = {
    'Dashboard': '/apps/syntherize',
    'Activity': '/apps/syntherize/program/activity',
    'Points': '/apps/syntherize/program/points',
    'Referrals': '/apps/syntherize/program/referrals',
    'Vip': '/apps/syntherize/program/vip',
    'Customers': '/apps/syntherize/customers',
    'Performance': '/apps/syntherize/performance',
    'Branding': '/apps/syntherize/performance',
    'CustomerEmail': '/apps/syntherize/customer_email',
    'Nudges': '/apps/syntherize/nudges',
    'Billing': '/apps/syntherize/billing',
}

const royalty_app_paths = [
    {
        path: paths.Dashboard,
        name: 'Dashboard',
        component: Dashboard
    }, {
        path: paths.Activity,
        name: 'Activity',
        component: Activity
    }, {
        path: paths.Points,
        name: 'Points',
        component: Points
    }, {
        path: paths.Referrals,
        name: 'Referrals',
        component: Referrals
    }, {
        path: paths.Vip,
        name: 'Vip',
        component: Vip
    }, {
        path: paths.Customers,
        name: 'Customers',
        component: Customers
    }, {
        path: paths.Performance,
        name: 'Performance',
        component: Performance
    }, {
        path: paths.Branding,
        name: 'Branding',
        component: Branding
    }, {
        path: paths.CustomerEmail,
        name: 'CustomerEmail',
        component: CustomerEmail
    }, {
        path: paths.Nudges,
        name: 'Nudges',
        component: Nudges
    }, {
        path: paths.Billing,
        name: 'Billing',
        component: Billing
    },
]

export default royalty_app_paths