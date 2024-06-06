<script setup> //This is a clue that this is the composition API, which is a new feature in Vue 3 to streamline defining components.
import {useToastStore} from '@/stores/toast'

const store = useToastStore()  //This is a store of state data.  Here it calls up the toast message, classes, and isVisible.

// return {
//     store
// }
</script>


<template>
    <div 
        v-if="store.isVisible"
        class="transition ease-in-out delay-500 duration-500 px-6 py-6 fixed top-full right-8 rounded-xl shadow-lg"
        :class="store.classes"
    >
        {{ store.message }}
    </div>

</template>