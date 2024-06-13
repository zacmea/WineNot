<template>
  <div v-if="collexn">
    <h1>{{ collexn.name }}</h1>
    <h2>Wines in this collection:</h2>
    <ul>
      <li v-for="wine in collexn.wines" :key="wine.id" class="flex items-center">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          fill="none"
          viewBox="0 0 24 24"
          stroke-width="1.5"
          stroke="currentColor"
          class="size-6 cursor-pointer mr-2"
          @click="removeWine(wine.id)"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            d="M6 18L18 6M6 6l12 12"
          />
        </svg>
        {{ wine.name }} - {{ wine.price }}
      </li>
    </ul>
  </div>
  <div v-else>
    <p>Loading...</p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'CollexnDetail',
  props: ['id'],
  data() {
    return {
      collexn: null,
      loading: true,
      error: null,
    }
  },
  async mounted() {
    this.getCollexnDetail();
  },
  methods: {
    async getCollexnDetail() {
      try {
        const response = await axios.get(`/api/collexns/${this.id}/`);
        this.collexn = response.data;
        // this.loading = false;
      } catch (error) {
        console.error(error);
        this.error = 'Failed to load collection details.';
        // this.loading = false;
      }
    },
    async removeWine(wineId) {
      try {
        await axios.post(`/api/collexns/${this.id}/remove_wine/${wineId}/`);
        this.collexn.wines = this.collexn.wines.filter(wine => wine.id !== wineId);
      } catch (error) {
        console.error(error);
        alert('Failed to remove wine from the collection.');
      }
    }
  }
}
</script>

<style>
.size-6 {
  width: 24px;
  height: 24px;
}
</style>
