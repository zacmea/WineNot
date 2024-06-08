<template>
    <nav class="py-10 px-8 border-b border-gray-200">
        <div class="max-w-7xl mx-auto">
            <div class="flex items-center justify-between">
                <div class="menu-left">
                    <a href="#" class="text-xl">{{ first_name }}</a>
                </div>
                <!-- NOTE: the below will only show if the user is authenticated -->
                <div class="menu-center flex space-x-12" v-if="userStore.user.isAuthenticated">
                    <RouterLink to="/">
                        <!-- NOTE: these svg snippets are icons from Heroicons, a collection of free, MIT-licensed icons from Tailwind makers.  The "path" attribute in the SVG tag gives the drawing instructions for the actual icon. Also avail. in jsx format-->
                        <svg
                            xmlns="http://www.w3.org/2000/svg"
                            fill="none"
                            viewBox="0 0 24 24"
                            stroke-width="2"
                            stroke="currentColor"
                            class="size-8"
                        >
                            <path
                                stroke-linecap="round"
                                stroke-linejoin="round"
                                d="M2.25 12l8.954-8.955c.44-.439 1.152-.439 1.591 0L21.75 12M4.5 9.75v10.125c0 .621.504 1.125 1.125 1.125H9.75v-4.875c0-.621.504-1.125 1.125-1.125h2.25c.621 0 1.125.504 1.125 1.125V21h4.125c.621 0 1.125-.504 1.125-1.125V9.75M8.25 21h8.25"
                            />
                        </svg>
                    </RouterLink>

                    <RouterLink to="/collexns">
                        <svg
                            xmlns="http://www.w3.org/2000/svg"
                            fill="none"
                            viewBox="0 0 24 24"
                            stroke-width="2"
                            stroke="currentColor"
                            class="size-8"
                        >
                            <path
                                stroke-linecap="round"
                                stroke-linejoin="round"
                                d="M8.25 6.75h12M8.25 12h12m-12 5.25h12M3.75 6.75h.007v.008H3.75V6.75Zm.375 0a.375.375 0 1 1-.75 0 .375.375 0 0 1 .75 0ZM3.75 12h.007v.008H3.75V12Zm.375 0a.375.375 0 1 1-.75 0 .375.375 0 0 1 .75 0Zm-.375 5.25h.007v.008H3.75v-.008Zm.375 0a.375.375 0 1 1-.75 0 .375.375 0 0 1 .75 0Z"
                            />
                        </svg>
                    </RouterLink>

                    <a href="#">
                        <svg
                            xmlns="http://www.w3.org/2000/svg"
                            fill="none"
                            viewBox="0 0 24 24"
                            stroke-width="2"
                            stroke="currentColor"
                            class="size-8"
                        >
                            <path
                                stroke-linecap="round"
                                stroke-linejoin="round"
                                d="M21 21l-5.197-5.197m0 0A7.5 7.5 0 105.196 5.196a7.5 7.5 0 0010.607 10.607z"
                            ></path>
                        </svg>
                    </a>
                </div>
                <!-- NOTE: this part controls the profile image and/or login/signup buttons -->
                <div class="menu-right">
                    <template v-if="userStore.user.isAuthenticated">
                        <RouterLink to="/profile">
                            <svg
                                xmlns="http://www.w3.org/2000/svg"
                                fill="none"
                                viewBox="0 0 24 24"
                                stroke-width="1.5"
                                stroke="currentColor"
                                class="size-9"
                            >
                                <path
                                    stroke-linecap="round"
                                    stroke-linejoin="round"
                                    d="M17.982 18.725A7.488 7.488 0 0 0 12 15.75a7.488 7.488 0 0 0-5.982 2.975m11.963 0a9 9 0 1 0-11.963 0m11.963 0A8.966 8.966 0 0 1 12 21a8.966 8.966 0 0 1-5.982-2.275M15 9.75a3 3 0 1 1-6 0 3 3 0 0 1 6 0Z"
                                />
                            </svg>
                        </RouterLink>
                    </template>

                    <template v-else>
                        <RouterLink
                            to="/login"
                            class="mr-4 py-4 px-6 bg-green-600 text-white rounded-lg"
                            >Log in
                        </RouterLink>
                        <RouterLink to="/signup" class="py-4 px-6 bg-blue-600 text-white rounded-lg"
                            >Sign up
                        </RouterLink>
                    </template>
                </div>
            </div>
        </div>
    </nav>

    <main class="px-8 py-6 bg-gray-100">
        <RouterView />
        <!-- NOTE: this is a placeholder for where the active routed component will be displayed -->
    </main>

    <Toast />
</template>

<script>
import axios from "axios";
import Toast from "@/components/Toast.vue";
import { useUserStore } from "@/stores/user";
import { RouterLink } from "vue-router";

export default {
    setup() {
        const userStore = useUserStore();

        return {
            userStore,
        };
    },

    components: {
        Toast,
    },

    beforeCreate() {
        this.userStore.initStore();

        const token = this.userStore.user.access;

        if (token) {
            axios.defaults.headers.common["Authorization"] = "Bearer " + token;
        } else {
            axios.defaults.headers.common["Authorization"] = "";
        }
    },
};
</script>
