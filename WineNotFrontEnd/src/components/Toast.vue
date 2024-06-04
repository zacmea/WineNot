<script setup>
import {useToastStore} from '@/stores/toast'

const store = useToastStore()

// return {
//     store
// }
</script>


<template>
    <div 
        v-if="store.isVisible"
        class="transition ease-in-out duration-500 delay-500 px-6 py-6 fixed top-full right-8 rounded-xl shadow-lg"
        :class="store.classes"
    >
        {{ store.message }}
    </div>

</template>