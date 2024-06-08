<template>
    <div>
        <h1>An unordered list of your collections is below:</h1>
        <br>
        <p>Would you like to add a new collection?</p>
        <form @submit.prevent="submitForm" method="post">
            <input type="text" v-model="form.name" placeholder="Name of collection" />
            
            <h3>Wines in collection:</h3>
            <div v-for="(wine, index) in form.wines" :key="index" class="wine-form">
                <input type="text" v-model="wine.name" placeholder="Wine name" />
                <input type="text" v-model="wine.link" placeholder="Wine link" />
                <input type="text" v-model="wine.thumb" placeholder="Wine thumb" />
                <input type="text" v-model="wine.country" placeholder="Wine country" />
                <input type="text" v-model="wine.region" placeholder="Wine region" />
                <input type="number" v-model.number="wine.average_rating" step="0.01" placeholder="Wine average rating" />
                <input type="number" v-model.number="wine.number_of_ratings" placeholder="Number of ratings" />
                <input type="number" v-model.number="wine.price" step="0.01" placeholder="Wine price" />
                <button type="button" @click="removeWine(index)">Remove</button>
                <br>
                <br>
            </div>
            <button type="button" @click="addWine">Add Wine</button>
            <br>
            <br>
            <button type="submit">Submit</button>
        </form>
        
        <ul>
            <li v-for="collexn in collexns" :key="collexn.id">
                <router-link :to="{ name: 'collexn-detail', params: { id: collexn.id } }">
                    {{ collexn.name }}
                </router-link>
            </li>
        </ul>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    name: 'ListOfCollexns',
    data() {
        return {
            form: {
                name: '',
                wines: [],
                created_by: { id: 1},
            },
            collexns: [],
        }
    },
    async mounted() {
        this.getCollexns();
    },
    methods: {
        async getCollexns() {
            try {
                const response = await axios.get('/api/collexns');
                console.log(response.data);
                this.collexns = response.data;
            } catch (error) {
                console.log(error);
            }
        },
        addWine() {
            this.form.wines.push({
                name: '',
                link: '',
                thumb: '',
                country: '',
                region: '',
                average_rating: '',
                number_of_ratings: '',
                price: '',
            });
        },
        removeWine(index) {
            this.form.wines.splice(index, 1);
        },
        prependHttp(url) {
            if (url && !/^https?:\/\//i.test(url)) {
                return 'http://' + url;
            }
            return url;
        },
        async submitForm() {
            // Prepend http:// to URL fields
            this.form.wines = this.form.wines.map(wine => ({
                ...wine,
                link: this.prependHttp(wine.link),
                thumb: this.prependHttp(wine.thumb),
                price: parseFloat(wine.price).toFixed(2), // Ensure price is a number with two decimal places
                average_rating: parseFloat(wine.average_rating).toFixed(2), // Ensure average_rating is a number with two decimal places
            }));

            console.log('form', this.form);
            try {
                const response = await axios.post('/api/collexns/create/', this.form);
                console.log('data', response.data);
                this.collexns.unshift(response.data);
                this.form.name = '';
                this.form.wines = [];
            } catch (error) {
                console.log('error', error);
            }
        }
    }
}
</script>

<style>
.wine-form {
    margin-bottom: 20px;
}
</style>
