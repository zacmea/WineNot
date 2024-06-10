<template>
    <div class="mx-auto flex flex-col gap-4">
        <div class="main-left">
            <div class="px-10 py-5 bg-white border border-gray-200 rounded-lg">
                <h1 class="mb-4 text-2xl text-center text-black font-semibold">LOGIN</h1>

                <p class="text-black max-w-7xl mb-3">
                    Welcome back! Wine not log in and plan for some wine-ing?
                </p>
                <!-- NOTE: the :to below is equivalent to v-bind:to, a shorthand for binding a value to a prop in Vue -->
                <p class="">
                    Don't have an account?
                    <RouterLink :to="{ name: 'signup' }" class="underline">Click here</RouterLink>
                    to create one!
                </p>
            </div>
        </div>

        <div class="main-right">
            <div class="p-12 bg-blue-100 border border-gray-200 pl-7 rounded-lg">
                <form class="space-y-6" v-on:submit.prevent="submitForm">
                    <div>
                        <label>E-mail</label><br />
                        <input
                            type="email"
                            v-model="form.email"
                            placeholder="Your e-mail address"
                            class="w-full mt-2 py-3 px-6 border border-gray-200 rounded-lg"
                        />
                    </div>

                    <div>
                        <label>Password</label><br />
                        <input
                            type="password"
                            v-model="form.password"
                            placeholder="Your password"
                            class="w-full mt-2 py-3 px-6 border border-gray-200 rounded-lg"
                        />
                    </div>

                    <template v-if="errors.length > 0">
                        <div class="bg-red-300 text-white rounded-lg p-6">
                            <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                        </div>
                    </template>

                    <div>
                        <button class="py-3 px-6 bg-blue-600 text-white rounded-xl">Log in</button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
import axios from "axios";

import { useUserStore } from "@/stores/user";

export default {
    setup() {
        const userStore = useUserStore();

        return {
            userStore,
        };
    },

    data() {
        return {
            form: {
                email: "",
                password: "",
            },
            errors: [],
        };
    },
    methods: {
        async submitForm() {
            this.errors = [];

            if (this.form.email === "") {
                this.errors.push("e-mail required");
            }

            if (this.form.password === "") {
                this.errors.push("password required");
            }

            if (this.errors.length === 0) {
                await axios
                    .post("/api/login/", this.form) //the form data is sent to the backend using axios
                    .then((response) => {
                        this.userStore.setToken(response.data); //in turn, the token is stored in the user store

                        console.log(response.data.access);

                        axios.defaults.headers.common["Authorization"] =
                            "Bearer " + response.data.access; //the token is then set as a header in axios, which will be used for all future requests
                    })
                    .catch((error) => {
                        console.log("error", error);
                    });

                await axios
                    .get("/api/me/") //a request is made to the backend to get the user information
                    .then((response) => {
                        this.userStore.setUserInfo(response.data); //the user information is stored in the user store

                        this.$router.push("/"); //NOTE: a router push is used to navigate to a different route, similar to a redirect
                    })
                    .catch((error) => {
                        console.log("error", error);
                    });
            }
        },
    },
};
</script>
