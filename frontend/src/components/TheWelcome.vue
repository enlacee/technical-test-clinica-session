
<script>
import TheHeader from '@/components/TheHeader.vue'

const VITE_APP_TITLE_HEADER = import.meta.env.VITE_APP_TITLE_HEADER;
const VITE_APP_AUTHOR_NAME = import.meta.env.VITE_APP_AUTHOR_NAME;
const VITE_APP_AUTHOR_URL = import.meta.env.VITE_APP_AUTHOR_URL;


export default {
    components: {
        TheHeader
    },
    data() {
        return {
            titleHeader: VITE_APP_TITLE_HEADER,
            authorName: VITE_APP_AUTHOR_NAME,
            authorURL: VITE_APP_AUTHOR_URL,
        }
    },
    mounted() {
        // this.$store.dispatch('refreshOwnerData');
    },
    methods: {
        // redirectToComponent (event) {
        //     const nameOfComponent = 'OneDate';
        //     this.$emit('changeCurrentComponent', nameOfComponent);
        // }
    },
    computed: {
        // ownerData() {
        //     return this.$store.getters.ownerData;
        // },
        // dataLoaded() {
        //     return this.$store.state.isLoading;
        // }
    }
}
</script>
<template>
    <div class="px-3 pt-6">
        <div v-show="dataLoaded">Cargando...</div>
        <div v-show="!dataLoaded">
            <header>
                <TheHeader :msg="titleHeader" />
            </header>

            <div class="w-full pt-2 pb-2">
                <h2 class="font-bold pb-2">1. Especialidades</h2>
                <div>
                    <button type="button" class="text-white bg-blue-700 hover:bg-blue-800  font-medium  text-sm px-4 py-2 mr-2 mb-2">Psicologia</button>
                    <button type="button" class="text-white bg-blue-700 hover:bg-blue-800  font-medium  text-sm px-4 py-2 mr-2 mb-2">Pediatria</button>
                    <button type="button" class="text-white bg-blue-700 hover:bg-blue-800  font-medium  text-sm px-4 py-2 mr-2 mb-2">Re al</button>
                    <button type="button" class="text-white bg-blue-700 hover:bg-blue-800  font-medium  text-sm px-4 py-2 mr-2 mb-2">Re al</button>
                    <button type="button" class="text-white bg-blue-700 hover:bg-blue-800  font-medium  text-sm px-4 py-2 mr-2 mb-2">Re al</button>
                    <button type="button" class="text-white bg-blue-700 hover:bg-blue-800  font-medium  text-sm px-4 py-2 mr-2 mb-2">Re al</button>
                </div>
            </div>
            <div>
                <h2 class="font-bold pb-2">2. Doctores</h2>
                <div>
                    <button type="button" class="text-white bg-blue-700 hover:bg-blue-800  font-medium  text-sm px-4 py-2 mr-2 mb-2">Dr Pepe</button>
                    <button type="button" class="text-white bg-blue-700 hover:bg-blue-800  font-medium  text-sm px-4 py-2 mr-2 mb-2">Dr Juan</button>
                    <button type="button" class="text-white bg-blue-700 hover:bg-blue-800  font-medium  text-sm px-4 py-2 mr-2 mb-2">Dra Maria</button>
                    <button type="button" class="text-white bg-blue-700 hover:bg-blue-800  font-medium  text-sm px-4 py-2 mr-2 mb-2">Dra Julia</button>
                </div>
            </div>

            <div>
                <h2 class="font-bold pb-2">3. Horario Disponible</h2>
                <div>
                    <form>
                        <label for="fecha">Fecha:</label>
                        <input type="date" id="fecha" name="fecha" required
                            class="shadow appearance-none border w-full_ py-2 px-3 text-gray-700 mb-3 leading-tight">

                        <label for="hora">Hora:</label>
                        <select id="hora" name="hora" required
                            class="shadow appearance-none border w-full_ py-2 px-3 text-gray-700 mb-3 leading-tight">
                        <option value="" disabled selected>Selecciona una hora</option>
                        <option value="10:00:00">10:00 AM</option>
                        <option value="11:00:00">11:00 AM</option>
                        <option value="12:00:00">12:00 PM</option>
                        <option value="13:00:00">01:00 PM</option>
                        <option value="14:00:00">02:00 PM</option>
                        <option value="15:00:00">03:00 PM</option>
                        <option value="16:00:00">04:00 PM</option>
                        <option value="17:00:00">05:00 PM</option>
                        </select>

                        <input type="submit" value="Confirmar cita"
                            class="bg-blue-700 hover:bg-blue-800 text-white py-2 px-4 focus:outline-none focus:shadow-outline w-full">
                    </form>
                </div>
            </div>




            <!-- <div class="w-full">
                <p class="mt-3 text-center text-gray-500 text-xs">
                    &copy;2023. All rights reserved. by <a target="_blank" :href="authorURL">{{ authorName }}</a>
                </p>
                <p class="text-center text-gray-500 text-xs">
                    <a :href="authorURL" target="_blank" class="text-sm text-blue-700">Contacto</a>
                </p>
            </div> -->
        </div>
    </div>
</template>