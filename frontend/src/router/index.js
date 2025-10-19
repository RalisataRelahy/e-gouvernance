import { createRouter, createWebHistory } from 'vue-router'
import Home from '../pages/acceuil.vue'
import ListCitizens from '../pages/list_citoyen.vue' 
import AddCitizen from '../pages/add_citoyen.vue'
import HeaderSection from '../components/header.vue'
import Info_user from '@/components/info_user.vue'
const routes = [
  { path: '/', component: Home },
  { path: '/add_citoyen', component: AddCitizen },
  { path: '/list_citoyen',component: ListCitizens},
  { path: '/header', component:HeaderSection},
  {
    path: '/info_user/:id',
    name: 'info_user',
    component: () => import('@/components/info_user.vue'),
    props: true
    }
]


const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
