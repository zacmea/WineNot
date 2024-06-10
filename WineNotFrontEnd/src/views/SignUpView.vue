<template>
    <div class="mx-auto flex flex-col gap-4">
        <div class="main-left">
            <div class="px-10 py-5 bg-white border border-gray-200 rounded-lg">
                <h1 class="mb-4 text-2xl text-center text-black font-semibold">SIGN UP</h1>

                <p class="text-black max-w-7xl">
                    Already have an account? <RouterLink :to="{ name: 'login' }" class="underline">Click here</RouterLink> to login
                </p>
            </div>
        </div>

        <form @submit.prevent="submitForm" class="bg-blue-100 pl-5  rounded-lg pt-3 text-black">
            <div>
                <label for="first_name">First Name</label>
                <br>
                <input type="text" id="first_name" v-model="form.first_name" required class="w-5/6 py-3 px-4 border  rounded-xl mb-4 mt-1"/>
            </div>
            <div>
                <label for="last_name">Last Name</label>
                <br>
                <input type="text" id="last_name" v-model="form.last_name" required class="w-5/6 py-3 px-4 border  rounded-xl mb-4 mt-1"/>
            </div>
            <div>
                <label for="email">Email</label>
                <br>
                <input type="email" id="email" v-model="form.email" required class="w-5/6 py-3 px-4 border  rounded-xl mb-4 mt-1"/>
            </div>
            <div>
                <label for="password1">Password</label>
                <br>
                <input type="password" id="password1" v-model="form.password1" required class="w-5/6 py-3 px-4 border  rounded-xl mb-4 mt-1"/>
            </div>
            <div>
                <label for="password2">Confirm Password</label>
                <br>
                <input type="password" id="password2" v-model="form.password2" required class="w-5/6 py-3 px-4 border  rounded-xl mb-4 mt-1"/>
            </div>

            <div v-if="errors.length > 0">
                <ul>
                    <li v-for="error in errors" :key="error">{{ error }}</li>
                </ul>
            </div>
            <div>
                <button type="submit" class="py-3 px-6 mb-3 bg-blue-600 text-white rounded-xl ">Sign Up</button>
            </div>
        </form>
    </div>
</template>

<script>
import axios from 'axios'

import { useToastStore } from '@/stores/toast'

export default {
    setup() {
        const toastStore = useToastStore()

        return {
            toastStore
        }
    },

    data() {
        return {
            form: {
                first_name: '',
                last_name: '',
                email: '',
                password1: '',
                password2: ''
            },
            errors: [],
        }
    },

    methods: {
        submitForm() {
            this.errors = []

            if (this.form.email === '') {
                this.errors.push('Your e-mail is missing')
            }

            if (this.form.first_name === '' || this.form.last_name === '') {
                this.errors.push('Your name is missing')
            }

            if (this.form.password1 === '') {
                this.errors.push('Your password is missing')
            }

            if (this.form.password1.length < 8) {
                this.errors.push('Your password must be at least 8 characters long')
            }

            if (this.form.password1 !== this.form.password2) {
                this.errors.push('The password does not match')
            }

            if (this.errors.length === 0) {
                // console.log('form', this.form);
                axios
                    .post('/api/signup/', this.form)
                    .then(response => {
                        if (response.data.message === 'success') {
                            this.toastStore.show(5000, 'The user is now registered. Please log in', 'bg-emerald-500')

                            this.form.first_name = ''
                            this.form.last_name = ''
                            this.form.email = ''
                            this.form.password1 = ''
                            this.form.password2 = ''
                        } else {
                            alert("Something went wrong.  Try checking that your password isn't too common and doesn't contain your name or email address.")
                            this.toastStore.show(5000, 'Something went wrong. Please try again', 'bg-red-300')
                        }
                    })
                    .catch(error => {
                        console.log('error', error)
                    })
            }
        }
    }
}
</script>