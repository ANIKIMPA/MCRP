import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import File from '../views/File.vue'
import MasterSchedule from '../views/MasterSchedule.vue'
import ListItem from '@/components/item/ListItem'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/files/:file',
    name: 'files',
    component: File
  },
  {
    path: '/master_schedule/:numberOfPeriods',
    name: 'master_schedule',
    component: MasterSchedule
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
  {
    path: '/items',
    name: 'ListItem',
    component: ListItem
  }
]

const router = new VueRouter({
  mode: 'history',
  routes
})

export default router
