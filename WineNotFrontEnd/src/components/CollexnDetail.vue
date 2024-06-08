<template>
  <div v-if="collexn">
    <h1>{{ collexn.name }}</h1>
    <h2>Wines in this collection:</h2>
    <ul>
      <li v-for="wine in collexn.wines" :key="wine.id">
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
      collexn: null
    }
  },
  async mounted() {
    this.getCollexnDetail();
  },
  methods: {
    async getCollexnDetail() {
      try {
        const response = await axios.get(`/api/collexns/${this.id}`);
        this.collexn = response.data;
      } catch (error) {
        console.error(error);
      }
    }
  }
}
</script>
