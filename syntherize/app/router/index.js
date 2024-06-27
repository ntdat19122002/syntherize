import {createRouter, createWebHistory} from 'vue-router'
import Dashboard from '../views/Dashboard.vue'
// Program
import Activity from '../views/Program/Activity.vue'
import Points from '../views/Program/Points.vue'
import Referrals from '../views/Program/Referrals.vue'
import Vip from '../views/Program/Vip.vue'
import Customers from '../views/Customers.vue'
import Performance from '../views/Performance.vue'
import Branding from '../views/Branding.vue'
import CustomerEmail from '../views/CustomerEmail.vue'
import Nudges from '../views/Nudges.vue'
import Billing from '../views/Billing.vue'
import paths from './paths'
import rest_api_paths from "./rest_api";

const router = createRouter({
    history: createWebHistory(),
    routes: [
        ...rest_api_paths,
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
})

export default router
