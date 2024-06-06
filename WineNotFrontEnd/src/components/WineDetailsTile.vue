<script setup>
import { ref } from 'vue';

const imageURL = ref('https://i.imgur.com/w398AJB.jpeg');
// import genericwinebottle from '../assets/genericwinebottle.jpg'

</script>

<template>
    <div class="flex flex-col items-center justify-center">
        <img :src="imageURL" alt="Generic wine bottle" class="w-1/2" />
        <h1 class="text-lg font-bold mt-8">WineName</h1>
        <p class="mt-2">WineDescription</p>
        <p class="mt-2">WinePrice</p>
    </div>
</template>