import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import BillOfMaterial from '@/components/billOfMaterial/DataGrid'
import MasterSchedule from '@/components/masterSchedule/DataGrid.vue'
import InventoryStatus from '@/components/inventoryStatus/DataGrid.vue'
import ItemMaster from '@/components/itemMaster/DataGrid.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/bill-of-material/:file',
    name: 'bill_of_material',
    component: BillOfMaterial
  },
  {
    path: '/master-schedule/:file',
    name: 'master_schedule',
    component: MasterSchedule
  },
  {
    path: '/inventory-status/:file',
    name: 'inventory_status',
    component: InventoryStatus
  },
  {
    path: '/item-master/:file',
    name: 'item_master',
    component: ItemMaster
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
  routes
})

export default router
