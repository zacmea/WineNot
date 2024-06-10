<template>
    <nav class="py-5 px-8 border-b border-gray-200">
        <div class="max-w-7xl mx-auto flex items-center justify-between">
            <!-- Empty div to take up space on the left -->
            <div class="flex-1"></div>

            <!-- Centered menu items -->
            <div
                class="menu-center flex space-x-8 flex-1 justify-center"
                v-if="userStore.user.isAuthenticated"
            >
                <RouterLink to="/">
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

                <RouterLink to="/search">
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
                </RouterLink>
            </div>

            <!-- Right aligned menu items -->
            <template v-if="userStore.user.isAuthenticated">
                <div class="menu-right flex-1 flex justify-end">
                    <div class="relative inline-block text-left" @click="toggleDropdown">
                        <RouterLink to="#">
                            <svg
                                xmlns="http://www.w3.org/2000/svg"
                                fill="none"
                                viewBox="0 0 24 24"
                                stroke-width="2.2"
                                stroke="currentColor"
                                class="size-7 -mr-4 text-blue-500"
                            >
                                <path
                                    stroke-linecap="round"
                                    stroke-linejoin="round"
                                    d="M17.982 18.725A7.488 7.488 0 0 0 12 15.75a7.488 7.488 0 0 0-5.982 2.975m11.963 0a9 9 0 1 0-11.963 0m11.963 0A8.966 8.966 0 0 1 12 21a8.966 8.966 0 0 1-5.982-2.275M15 9.75a3 3 0 1 1-6 0 3 3 0 0 1 6 0Z"
                                />
                            </svg>
                        </RouterLink>
                        <div
                            v-if="dropdownOpen"
                            class="origin-top-right absolute right-0 mt-2 w-56 rounded-md shadow-lg bg-white ring-1 ring-black ring-opacity-5 focus:outline-none"
                        >
                            <div
                                class="py-1"
                                role="menu"
                                aria-orientation="vertical"
                                aria-labelledby="options-menu"
                            >
                                <router-link
                                    to="/profile"
                                    class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100"
                                    role="menuitem"
                                    >Profile</router-link
                                >
                                <a
                                    @click="logout"
                                    class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 cursor-pointer"
                                    role="menuitem"
                                    >Log Out</a
                                >
                            </div>
                        </div>
                    </div>
                </div>
            </template>
        </div>
    </nav>
<template v-if="!userStore.user.isAuthenticated">
    <div class="justify-center align-middle">
        <h1 class="text-center text-sm">Welcome! Please log in or sign up to continue.</h1>
    </div>
</template>
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
    data() {
        return {
            dropdownOpen: false,
        };
    },
    methods: {
        toggleDropdown() {
            this.dropdownOpen = !this.dropdownOpen;
        },
        logout() {
            this.userStore.removeToken();
            this.$router.push("/login");
        },
    },

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
