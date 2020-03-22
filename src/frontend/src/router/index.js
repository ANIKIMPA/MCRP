import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from '../views/Login.vue'
import Register from '../views/Register.vue'
import Home from '../views/Home.vue'
import BillOfMaterial from '@/components/billOfMaterial/DataGrid'
import MasterSchedule from '@/components/masterSchedule/DataGrid.vue'
import InventoryStatus from '@/components/inventoryStatus/DataGrid.vue'
import ItemMaster from '@/components/itemMaster/DataGrid.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/register',
    name: 'register',
    component: Register,
    meta: {
      requiresLogged: true
    }
  },
  {
    path: '/login',
    name: 'login',
    component: Login,
    meta: {
      requiresLogged: true
    }
  },
  {
    path: '/',
    name: 'home',
    component: Home,
    meta: {
      requiresAuth: true
    }
  },
  {
    path: '/bill-of-material/:file',
    name: 'bill_of_material',
    component: BillOfMaterial,
    meta: {
      requiresAuth: true
    }
  },
  {
    path: '/master-schedule/:file',
    name: 'master_schedule',
    component: MasterSchedule,
    meta: {
      requiresAuth: true
    }
  },
  {
    path: '/inventory-status/:file',
    name: 'inventory_status',
    component: InventoryStatus,
    meta: {
      requiresAuth: true
    }
  },
  {
    path: '/item-master/:file',
    name: 'item_master',
    component: ItemMaster,
    meta: {
      requiresAuth: true
    }
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
