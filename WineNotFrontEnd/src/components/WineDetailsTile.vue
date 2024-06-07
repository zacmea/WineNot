<script setup>
import { ref } from 'vue';

const imageURL = ref('https://i.imgur.com/w398AJB.jpeg');
// import genericwinebottle from '../assets/genericwinebottle.jpg'

</script>

<!-- TURN THE BELOW INTO A CARD, using v-card, v-img, v-card-title, v-card-text, v-card-actions, v-btn -->

<template>
    <div class="rounded-lg bg-slate-500 p-5 grid-rows-5 rows-5 columns-2 grid-flow-col gap-4">

        <img :src="imageURL" alt="Generic wine bottle" class="rounded-2xl row-span-3" />

        <div id="rightColumn" class="block">
            <div class="" style="break-before: column; font-weight: bold">
                <h1 class="text-2xl">WineName</h1>
            </div>
            <div class=" mt-5 pt-5">Wine Description</div>
            <br>
            <br>
            <br>
            <div class="relative mt-20 ml-20 h-20 w-20">
                <div class="absolute bottom-0 right-0 text-end" style="break-before: row;">Wine price</div>
            </div>
        </div>
        <!-- end of rightColumn -->
    </div>



</template>