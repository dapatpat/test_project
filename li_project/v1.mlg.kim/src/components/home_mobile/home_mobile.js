import Swiper from '../../../static/lib/swiper/swiper.min.js'

export default {
    data () {
        return {
            name: 11
        }
    },
    methods: {
        swiper () {
            new Swiper('.swiper-container', {
                autoplay: 1000,
                loop: true,
                observer: true
            })
        }
    },
    created () {
        console.log('created2')
    },
    mounted () {
        this.swiper()
    }
}
