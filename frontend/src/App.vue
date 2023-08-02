<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { isMobile  } from '@/utils/validate';
</script>
<template>
    <div class="wrapper">
        <div v-if="isMobile() == false" class="web shadow">
            <!-- <Home/> -->
            <RouterView />
        </div>
        <div v-if="isMobile() == true" class="w-full">
            <!-- <Home/> -->
            <RouterView />
        </div>
    </div>
</template>
<style scoped>
.wrapper{
    display: flex;
    flex-flow: column wrap;
    align-items: center;
    width: 100%;
    min-height: 100vh;
}

.wrapper > div {
    background-color: white;
    min-height: 100vh;
}
.web{
    width: 481px;
    max-width: 481px;
}
</style>