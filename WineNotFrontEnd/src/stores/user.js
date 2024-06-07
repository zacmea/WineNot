//This file contains the user store, which is used to store the user's information and tokens. It also contains methods to set and remove the tokens, set the user information, and refresh the token.

import {defineStore} from 'pinia'
import axios from 'axios'

export const useUserStore = defineStore({
    id: 'user',

    state: () => ({
        user: {
            isAuthenticated: false,
            id: null,
            first_name: '',
            last_name: '',
            email: '',
            access: null,  // access token
            refresh: null  // refresh token
        }
    }),

    actions: {
        initStore() {
            console.log('initStore');
            if (localStorage.getItem('user.access')) {
                this.user.access = localStorage.getItem('user.access')
                this.user.refresh = localStorage.getItem('user.refresh')
                this.user.id = localStorage.getItem('user.id')
                this.user.first_name = localStorage.getItem('user.first_name')
                this.user.last_name = localStorage.getItem('user.last_name')
                this.user.email = localStorage.getItem('user.email')
                this.user.isAuthenticated = true

                this.refreshToken()

                console.log('User store initialized', this.user);
            }
        },

        setToken(data) {
            console.log('setting token', data);
            this.user.access = data.access
            this.user.refresh = data.refresh
            this.user.isAuthenticated = 
            localStorage.setItem('user.access', data.access)
            localStorage.setItem('user.refresh', data.refresh)
        },

        removeToken() {
            this.user.access = null
            this.user.refresh = null
            this.user.isAuthenticated = false

            localStorage.removeItem('user.access')
            localStorage.removeItem('user.refresh')
            localStorage.removeItem('user.id')
            localStorage.removeItem('user.firstName')
            localStorage.removeItem('user.lastName')
            localStorage.removeItem('user.email')
        },

        setUserInfo(user) {
            console.log('setting user info', user);

            this.user.id = user.id
            this.user.first_name = user.first_name
            this.user.last_name = user.last_name
            this.user.email = user.email

            localStorage.setItem('user.id', user.id)
            localStorage.setItem('user.first_name', user.first_name)
            localStorage.setItem('user.last_name', user.last_name)
            localStorage.setItem('user.email', user.email)

            console.log('User store updated', this.user);
        },

        refreshToken() {  //this will keep the user logged in
            axios.post('/api/refresh/', {
                refresh: this.user.refresh
            })
            .then((response) => {
                this.user.access = response.data.access

                localStorage.setItem('user.access', response.data.access)

                    axios.defaults.headers.common["Authorization"] = "Bearer " + response.data.access
            })
            .catch((error) => {
                console.log('Error refreshing token', error);
                this.removeToken()
            })
        },
    }
})