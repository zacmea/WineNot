<template>
    <div>
        <h1 class="text-center font-bold text-3xl -mt-2">Your collections</h1>
        <br />
        <p class="font-extralight">Would you like to add a new collection?</p>
        <form @submit.prevent="submitForm" method="post">
            <input class="pl-2 mt-1 rounded-lg" type="text" v-model="form.name" placeholder="Name of collection" />

            <h3 class="font-extralight text-right mt-1">Wines in collection:</h3>
            <div v-for="(wine, index) in form.wines" :key="index" class="wine-form">
                <input type="text" v-model="wine.name" placeholder="Wine name" />
                <input type="text" v-model="wine.link" placeholder="Wine link" />
                <input type="text" v-model="wine.thumb" placeholder="Wine thumb" />
                <input type="text" v-model="wine.country" placeholder="Wine country" />
                <input type="text" v-model="wine.region" placeholder="Wine region" />
                <input
                    type="number"
                    v-model.number="wine.average_rating"
                    step="0.01"
                    placeholder="Wine average rating"
                />
                <input
                    type="number"
                    v-model.number="wine.number_of_ratings"
                    placeholder="Number of ratings"
                />
                <input
                    type="number"
                    v-model.number="wine.price"
                    step="0.01"
                    placeholder="Wine price"
                />
                <button type="button" @click="removeWine(index)">Remove</button>
                <br />
                <br />
            </div>
            <div class="flex justify-end">
                <button
                    type="button"
                    @click="addWine"
                    class="border 2 border-blue-200 italic rounded-xl px-3 font-extralight text-sm"
                >
                    Add Wine
                </button>
            </div>
            <div class="font-semibold flex justify-center ">
            <button class="border-2 border-blue-300 rounded-xl bg-blue-200 px-2 text-lg" type="submit">Submit</button>
            </div>
        </form>
        <hr class="border-t-2 border-blue-200 my-3"/>
        <ul>
            <li v-for="collexn in collexns" :key="collexn.id" class="flex items-center">
                <svg
                    xmlns="http://www.w3.org/2000/svg"
                    fill="none"
                    viewBox="0 0 24 24"
                    stroke-width="1.5"
                    stroke="currentColor"
                    class="size-3.5 cursor-pointer"
                    @click="deleteCollexn(collexn.id)"
                >
                    <path
                        stroke-linecap="round"
                        stroke-linejoin="round"
                        d="m14.74 9-.346 9m-4.788 0L9.26 9m9.968-3.21c.342.052.682.107 1.022.166m-1.022-.165L18.16 19.673a2.25 2.25 0 0 1-2.244 2.077H8.084a2.25 2.25 0 0 1-2.244-2.077L4.772 5.79m14.456 0a48.108 48.108 0 0 0-3.478-.397m-12 .562c.34-.059.68-.114 1.022-.165m0 0a48.11 48.11 0 0 1 3.478-.397m7.5 0v-.916c0-1.18-.91-2.164-2.09-2.201a51.964 51.964 0 0 0-3.32 0c-1.18.037-2.09 1.022-2.09 2.201v.916m7.5 0a48.667 48.667 0 0 0-7.5 0"
                    />
                </svg>
                <router-link
                    :to="{ name: 'collexn-detail', params: { id: collexn.id } }"
                    class="ml-2 text-xl py-0.5"
                >
                    {{ collexn.name }}
                </router-link>
            </li>
        </ul>
    </div>
</template>

<script>
import axios from "axios";

export default {
    name: "ListOfCollexns",
    data() {
        return {
            form: {
                name: "",
                wines: [],
                created_by: { id: 1 },
            },
            collexns: [],
        };
    },
    async mounted() {
        this.getCollexns();
    },
    methods: {
        async getCollexns() {
            try {
                const response = await axios.get("/api/collexns");
                console.log(response.data);
                this.collexns = response.data;
            } catch (error) {
                console.log(error);
            }
        },
        addWine() {
            this.form.wines.push({
                name: "",
                link: "",
                thumb: "",
                country: "",
                region: "",
                average_rating: "",
                number_of_ratings: "",
                price: "",
            });
        },
        removeWine(index) {
            this.form.wines.splice(index, 1);
        },
        prependHttp(url) {
            if (url && !/^https?:\/\//i.test(url)) {
                return "http://" + url;
            }
            return url;
        },
        async submitForm() {
            // Prepend http:// to URL fields
            this.form.wines = this.form.wines.map((wine) => ({
                ...wine,
                link: this.prependHttp(wine.link),
                thumb: this.prependHttp(wine.thumb),
                price: parseFloat(wine.price).toFixed(2), // Ensure price is a number with two decimal places
                average_rating: parseFloat(wine.average_rating).toFixed(2), // Ensure average_rating is a number with two decimal places
            }));

            console.log("form", this.form);
            try {
                const response = await axios.post("/api/collexns/create/", this.form);
                console.log("data", response.data);
                this.collexns.unshift(response.data);
                this.form.name = "";
                this.form.wines = [];
            } catch (error) {
                console.log("error", error);
            }
        },
        async deleteCollexn(id) {
            try {
                await axios.delete(`/api/collexns/${id}/delete/`);
                this.collexns = this.collexns.filter((collexn) => collexn.id !== id);
            } catch (error) {
                console.log("error", error);
            }
        },
    },
};
</script>

<style>
.wine-form {
    margin-bottom: 20px;
}
.size-6 {
    width: 24px;
    height: 24px;
}
</style>
