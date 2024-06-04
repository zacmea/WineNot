<template>
    <h1>SIGN UP</h1>

    <p>Already have an account? <RouterLink :to="{ 'name': 'login' }">Click here</RouterLink> to login</p>

    <form v-on:submit.prevent="submitForm">
        <div>
            <label for="first_name">First Name</label>
            <input type="text" id="first_name" v-model="form.first_name" required>
        </div>
        <div>
            <label for="last_name">Last Name</label>
            <input type="text" id="last_name" v-model="form.last_name" required>
        </div>
        <div>
            <label for="email">Email</label>
            <input type="email" id="email" v-model="form.email" required>
        </div>
        <div>
            <label for="password1">Password</label>
            <input type="password" id="password1" v-model="form.password1" required>
        </div>
        <div>
            <label for="password2">Confirm Password</label>
            <input type="password" id="password2" v-model="form.password2" required>
        </div>

        <div v-if="errors.length > 0">
            <ul>
                <li v-for="error in errors" v-bind:key="error">{{ error }}</li>
            </ul>
        </div>

        <button type="submit">Sign Up</button>
    </form>
</template>

<script>
import axios from 'axios';

export default {
    setup() {
        const toastStore = useToastStore();

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
            errors: [],  //create an array to store errors to show to the user
        }
    },
    methods: {
        submitForm() {
            this.errors = [];

            if this.form.first_name === '' || this.form.last_name === ''{
                this.errors.push('First and last name required');
            }
            if this.form.email === '' {
                this.errors.push('Email is required');
            }
            if this.form.password1 === '' {
                this.errors.push('Password is required');
            }
            if this.form.password2 !== this.form.password1 {
                this.errors.push('Passwords do not match');
            }      
            
            if (this.errors.length === 0) {
                axios
                    .post('/api/register/', this.form)
                    .then(response => {
                        if (Response.data.message === 'success') {
                            this.toastStore.show(5000, 'Account created successfully', 'bg-green-500');
                            this.form.first_name = '';
                            this.form.last_name = '';
                            this.form.email = '';
                            this.form.password1 = '';
                            this.form.password2 = '';
                        } else {
                            this.toastStore.show(5000, 'Account creation failed', 'bg-red-500');
                        }

    }
}
</script>