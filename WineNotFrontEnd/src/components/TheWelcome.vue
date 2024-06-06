<script setup>
import WelcomeItem from './WelcomeItem.vue'
import DocumentationIcon from './icons/IconDocumentation.vue'
import ToolingIcon from './icons/IconTooling.vue'
import EcosystemIcon from './icons/IconEcosystem.vue'
import CommunityIcon from './icons/IconCommunity.vue'
import SupportIcon from './icons/IconSupport.vue'
</script>

<template>

    <body class="bg-blue-400 text-center text-3xl">
        <template v-if="currentUser">
            <h1>Welcome, {{ currentUser.name }}!</h1>
            <div>
                <a class="a" href="/collexns">View your collections</a>
                <a class="a" href="/wines">Browse wines</a>
            </div>
        </template>
        <template v-else>
           <div class="mb-10 pt-5">
            <h1>Welcome!</h1>
            <h2>Wanna talk about wines?  Wine not!</h2>
            </div>
            <div>
                <RouterLink to="/login" class="mr-4 py-4 px-6 bg-gray-600 text-white rounded-lg">Log in</RouterLink>
                <RouterLink to="/signup" class="py-4 px-6 bg-purple-600 text-white rounded-lg">Sign up</RouterLink>
            </div>
        </template>
    </body>
</template>
