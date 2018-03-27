import Vue from 'vue'
import Router from 'vue-router'
import HomeMobile from '@/components/home_mobile/home_mobile.vue'
import Submit from '@/components/agency/submit/submit.vue'
import Board from '@/components/agency/board/board.vue'
import Detail from '@/components/agency/detail/detail.vue'
import Info from '@/components/agency/info/info.vue'
import List from '@/components/agency/list/list.vue'


Vue.use(Router)

export default new Router({
    routes: [
        {
            path: '/',
            name: 'homeMobile',
            component: HomeMobile
        },
        {
            path: '/agency/board',
            name: 'board',
            component: Board
        },
        {
            path: '/agency/detail',
            name: 'detail',
            component: Detail
        },
        {
            path: '/agency/info',
            name: 'info',
            component: Info
        },
        {
            path: '/agency/list',
            name: 'list',
            component: List
        },
        {
            path: '/agency/submit',
            name: 'submit',
            component: Submit
        }
    ]
})
