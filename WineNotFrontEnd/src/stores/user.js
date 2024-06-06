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
            accessToken: null,
            refreshToken: null
        }
    }),

    actions: {
        initStore() {
            if (localStorage.getItem('user')) {
                this.user.accessToken = localStorage.getItem('user.accessToken')
                this.user.refreshToken = localStorage.getItem('user.refreshToken')
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
            this.user.accessToken = data.accessToken
            this.user.refreshToken = data.refreshToken
            this.user.isAuthenticated = true

            localStorage.setItem('user.accessToken', data.accessToken)
            localStorage.setItem('user.refreshToken', data.refreshToken)
        },

        removeToken() {
            this.user.accessToken = null
            this.user.refreshToken = null
            this.user.isAuthenticated = false

            localStorage.removeItem('user.accessToken')
            localStorage.removeItem('user.refreshToken')
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

        refreshToken() {
            axios.post('/api/account/refresh', {
                refreshToken: this.user.refreshToken
            })
            .then((response) => {
                this.user.accessToken = response.data.accessToken

                localStorage.setItem('user.accessToken', response.data.accessToken)

                axios.defaults.headers.common['Authorization'] = `Bearer ${response.data.accessToken}`
            })
            .catch((error) => {
                console.log('Error refreshing token', error);
                this.removeToken()
            })
        },
    }
})