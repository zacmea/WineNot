<template>
    <div v-if="userStore.user.isAuthenticated">
        <div class="bg-blue-200 text-center text-3xl rounded-lg pb-6">
            <h1 class="py-4">Profile</h1>
            <p class="text-2xl pb-4">Name: {{ profile.first_name }} {{profile.last_name}}</p>
            <!-- <p class="text-2xl pb-4"> -->
            <p class="text-2xl pb-4">Email: {{ profile.email }}</p>
        </div>
    </div>
    <div v-else>
        <p>Please log in to view your profile.</p>
        <RouterLink to="/login" class="mr-4 py-4 px-6 bg-green-600 text-white rounded-lg">Log in</RouterLink>
    </div>
</template>

<script>
import { useUserStore } from '@/stores/user';
import axios from 'axios';

export default {
    name: 'ProfilePage',
    data() {
        return {
            profile: {}
        }
    },
    setup() {
        const userStore = useUserStore()

        return {
            userStore
        }
    },
    async mounted() {
        if (this.userStore.user.isAuthenticated) {
            await this.fetchUserProfile();
        }
    },
    methods: {
        async fetchUserProfile() {
            try {
                const response = await axios.get('/api/me');
                this.profile = response.data;
            } catch (error) {
                console.error(error);
            }
        }
    }
}
</script>

<style>
/* Add your styles here */
</style>
