<script setup>
import { onMounted } from 'vue'
import { initFlowbite } from 'flowbite'

const VITE_API_FLASK_ENDPOINT = import.meta.env.VITE_API_FLASK_ENDPOINT;

// initialize components based on data attribute selectors
onMounted(() => {
    initFlowbite();
})

let checkForm = function() {
    console.log('click o submit');
    document.querySelector('#closeButton').click(); // close modal
    document.forms["patient-data"].elements["data-filled"].value = 1; // set status form (filled)
    return false;
}

</script>
<template>
    <div>
        <!-- Hidden the Button to open modal -->
        <div class="flex justify-center p-4 hidden">
            <button id="button-show-modal" data-modal-toggle="modal" data-modal-target="modal" 
            type="button" class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 mr-2 mb-2 dark:bg-blue-600 dark:hover:bg-blue-700 focus:outline-none dark:focus:ring-blue-800">Show modal</button>
        </div>

        <div id="modal"
            tabindex="-1"
            aria-hidden="true"
            class="fixed top-0 left-0 right-0 z-50 hidden w-full p-4 overflow-x-hidden overflow-y-auto md:inset-0 h-[calc(100%-1rem)] max-h-full">
            <div class="relative w-full max-w-2xl max-h-full">
                <!-- Modal content -->
                <div class="relative bg-white rounded-lg shadow dark:bg-gray-700">

                    <!-- Modal header -->
                    <div class="flex items-start justify-between p-5 border-b rounded-t dark:border-gray-600">
                        <h3 class="text-xl font-semibold text-gray-900 lg:text-2xl dark:text-white">
                            Antes: Llenar los datos del paciente
                        </h3>
                        <button id="closeButton" data-modal-hide="modal" type="button" class="text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm p-1.5 ml-auto inline-flex items-center dark:hover:bg-gray-600 dark:hover:text-white">
                            <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd"></path></svg>  
                        </button>
                    </div>
                    <!-- Modal body -->
                    <div class="p-5 space-y-5">
                        <div>
                            <form name="patient-data" class="bg-white" action="javascript:void(0);"  @submit="checkForm">
                                <input type="hidden" value="0" id="data-filled" name="data-filled">

                                <div class="mb-4">
                                    <label class="block text-gray-700 text-sm mb-2" for="name">
                                        Nombres:
                                    </label>
                                    <input class="shadow appearance-none border w-full py-2 px-3 text-gray-700 leading-tight"
                                        oninput="this.value = this.value.replace(/[^A-Za-z]/g, '')"
                                        id="name" name="name" type="text" required>
                                </div>
                                <div class="mb-4">
                                    <label class="block text-gray-700 text-sm mb-2" for="lastname">
                                        Apellidos:
                                    </label>
                                    <input class="shadow appearance-none border w-full py-2 px-3 text-gray-700 leading-tight"
                                        oninput="this.value = this.value.replace(/[^A-Za-z]/g, '')"
                                        id="lastname" name="lastname" type="text" required>
                                </div>
                                <div class="mb-4">
                                    <label class="block text-gray-700 text-sm mb-2" for="email">
                                        Correo electrónico:
                                    </label>
                                    <input class="shadow appearance-none border w-full py-2 px-3 text-gray-700 leading-tight"
                                        type="email" id="email" name="email" required>
                                </div>

                                <div class="mb-4">
                                    <label class="block text-gray-700 text-sm mb-2" for="phone">
                                        Telefono:
                                    </label>
                                    <input class="shadow appearance-none border w-full py-2 px-3 text-gray-700 leading-tight"
                                        type="tel" id="phone" name="phone" pattern="[0-9]{7,}" 
                                        oninput="this.value = this.value.replace(/[^0-9]/g, '')"
                                        minlength="7"
                                        required>
                                </div>

                                <div class="flex items-center justify-between mt-9 mb-5">
                                    <button class="bg-blue-700 hover:bg-blue-800 text-white py-2 px-4 focus:outline-none focus:shadow-outline w-full"
                                        type="submit">
                                        Confirmar cita
                                    </button>
                                </div>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>