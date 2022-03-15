import * as Vue from 'vue'
import App from './App.vue'
import router from '@/router'
import { createProvider } from './vue-apollo'

new Vue({
    router,
    apolloProvider: createProvider(),
    render: h => h(App)
}).$mount('#app');

