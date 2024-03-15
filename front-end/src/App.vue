<script setup lang="ts">
import Header from './components/Header.vue';
import Hero from "./components/Hero.vue";
import { onMounted } from 'vue';
import { initFlowbite } from 'flowbite';

// initialize components based on data attribute selectors
onMounted(() => {
    initFlowbite();
})
</script>

<template>
  <Header />
  <Hero />
</template>

<style scoped>
</style>
