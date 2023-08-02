<script setup>
defineProps({
  msg: {
    type: String,
    required: true
  }
})
</script>

<template>
  <div class="text-center">
    
    <h1 class="text-xl font-bold dark:text-white mb-2">
        {{ msg }}
    </h1>
    <p class="text-gray-500 text-md mb-2">
        ¡Sistema de reserva de citas médicas en línea! Estamos encantados de ayudarte a programar tu próxima consulta con uno de nuestros especialistas.
    </p>
  </div>
</template>