<template>
  <Splashscreen/>
  <Header/>
<main>
  <router-view></router-view>
</main>

</template>
<script setup>
import Header from './components/header.vue';
import Splashscreen  from './components/splashscreen.vue';
</script>