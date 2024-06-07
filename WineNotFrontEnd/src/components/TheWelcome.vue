<template>

    <body class="bg-blue-300 text-center text-3xl rounded-lg">
        <template v-if="userStore.user.isAuthenticated">
            <h1>Welcome, {{ userStore.user.first_name }}!</h1>
            <div>
                <RouterLink to="/collexns">View your collections</RouterLink>
                <RouterLink to="/wines">Browse wines</RouterLink>
            </div>
        </template>
        <template v-else>
           <div class="mb-10 pt-5">
            <h1>Welcome!</h1>
            <h2>Wanna talk about wines?  Wine not!</h2>
            </div>
            <div>
                <RouterLink to="/login" class="mr-4 py-4 px-6 bg-green-600 text-white rounded-lg">Log in</RouterLink>
                <RouterLink to="/signup" class="py-4 px-6 bg-blue-600 text-white rounded-lg">Sign up</RouterLink>
            </div>
        </template>
    </body>
</template>

<script>
    import axios from 'axios'
    import Toast from '@/components/Toast.vue'
    import { useUserStore } from '@/stores/user'

    export default {
        setup() {
            const userStore = useUserStore()

            return {
                userStore
            }
        },

        components: {
            Toast
        },

        beforeCreate() {
            this.userStore.initStore()

            const token = this.userStore.user.access

            if (token) {
                axios.defaults.headers.common["Authorization"] = "Bearer " + token;
            } else {
                axios.defaults.headers.common["Authorization"] = "";
            }
        }
    }
</script>
