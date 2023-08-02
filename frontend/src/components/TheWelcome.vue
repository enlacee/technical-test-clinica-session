
<script>
import TheHeader from '@/components/TheHeader.vue'
import PopUpPatientData from '@/components/shared/PopUpPatientData.vue'
import EspecialidadService from '@/services/EspecialidadService';
import EspecialistaService from '@/services/EspecialistaService';
import SesionService from '@/services/SesionService';

const VITE_APP_TITLE_HEADER = import.meta.env.VITE_APP_TITLE_HEADER;
const VITE_APP_AUTHOR_NAME = import.meta.env.VITE_APP_AUTHOR_NAME;
const VITE_APP_AUTHOR_URL = import.meta.env.VITE_APP_AUTHOR_URL;


export default {
    components: {
        TheHeader,
        PopUpPatientData
    },
    data() {
        return {
            titleHeader: VITE_APP_TITLE_HEADER,
            authorName: VITE_APP_AUTHOR_NAME,
            authorURL: VITE_APP_AUTHOR_URL,
            isLoading: true,
            especialidades: [],
            especialistas: [],
        }
    },
    mounted() {
        this.fetchDataEspecialidades();
    },
    methods: {
        fetchDataEspecialidades: function(){
            EspecialidadService.get()
                .then((data) => {
                    this.isLoading = false;
                    this.especialidades = data;
                })
                .catch((error) => {
                    console.error(error);
                    this.especialidades = [];
                });
        },
        fetchDataEspecialistasPorEspecialidadId: function(especialidad_id){
            let params = { especialidad: especialidad_id };

            EspecialistaService.get(params)
                .then((data) => {
                    this.especialistas = data;
                })
                .catch((error) => {
                    console.error(error);
                    this.especialistas = [];
                });
        },
        /**
         * HTML
         */

        /**
         * Open modal
         *
         * @return void
         **/
        showPopUp: function(){
            document.querySelector('#button-show-modal').click();
        },

        /**
         * Selecccionar especialidad
         *
         * @return void
         **/
        selectEspecialidad: function(event){
            let numberSelected = parseInt(event.target.getAttribute('aria-label'));
            document.querySelectorAll('#especialidades button').forEach(boton => boton.classList.remove('selected'));
            document.querySelector(`#especialidades button[aria-label="${numberSelected}"]`).classList.toggle("selected");

            // cargar datos de doctores
            this.fetchDataEspecialistasPorEspecialidadId(numberSelected);
        },

        /**
         * Selecccionar especialista
         *
         * @return void
         **/
        selectEspecialista(event) {
            let numberSelected = parseInt(event.target.getAttribute('aria-label'));
            document.querySelectorAll('#especialistas button').forEach(boton => boton.classList.remove('selected'));
            document.querySelector(`#especialistas button[aria-label="${numberSelected}"]`).classList.toggle("selected");

            this.$refs.Disponible.style.display = 'block';
        },

        /**
         * Valid form data, following the HTML-FORM flow
         *
         * @return void
         **/
        confirmSesion() {
            if (
                document.getElementById('fecha').value.length === 0 ||
                document.getElementById('hora').value.length === 0
            ) {
                return true;
            }

            // Validar si los datos del paciente ya estan cargados SINO enviar datos
            if (this.isPatientDataFilled() === false) {
                this.showPopUp()
            } else {
                this.sendDataToServer();
            }
        },

        /**
         * Send data to server
         *
         * @return void
         **/
        sendDataToServer() {
            console.log('request preguntar si esta disponible y sino INSERT DATA')
            let getAllDataNeeded = function(){
                let $patientForm = document.forms["patient-data"];
                const botonSeleccionado = document.querySelector('#especialistas button.selected');
                const especialista_id = botonSeleccionado ? botonSeleccionado.getAttribute('aria-label') : '';
                let fecha_hora = document.querySelector('#fecha').value + ' ' + document.querySelector('#hora').value;
                let paciente_nombre = $patientForm.elements["name"].value.trim() + ' ';
                paciente_nombre += $patientForm.elements["lastname"].value.trim();
                let paciente_data = {
                    "nombre": $patientForm.elements["name"].value.trim(),
                    "apellido": $patientForm.elements["lastname"].value.trim(),
                    "correo": $patientForm.elements["email"].value.trim(),
                    "telefono": $patientForm.elements["phone"].value.trim()
                };

                return {
                    'especialista_id': especialista_id,
                    'fecha_hora': fecha_hora,
                    'paciente_nombre': paciente_nombre,
                    'paciente_data': paciente_data
                };
            };

            let params = getAllDataNeeded();
            console.log('params', params)

            if (params['especialista_id'].length > 0) {
                SesionService.post(params)
                .then((data) => {
                    if (data.error) {
                        alert(data.error);
                    } else if (data.mensaje) {
                        alert(data.mensaje);
                        window.location.href = '/';
                    }
                    console.log('SesionService data', data)
                    console.log('SesionService data', data.mensaje)
                    console.log('SesionService data', data.error)
                })
                .catch((error) => {
                    console.error(error);
                });
            } else {
                alert("Debe seleccione 1 especialista");
            }

            return true
        },

        /**
         * Get status if form is filled
         *
         * @return booleam
         **/
        isPatientDataFilled() {
            let flag = parseInt(document.forms["patient-data"].elements["data-filled"].value);
            let result = false;
            if ( flag == 1 ) {
                result = true;
            }
            return result
        }

    },
    computed: {
        dataLoaded() {
            return false;
        }
    },
}
</script>
<template>
    <div class="px-2 pt-2">
        <div v-show="isLoading">Cargando...</div>
        <div v-show="!isLoading">
            <header>
                <TheHeader :msg="titleHeader" />
            </header>

            <div class="w-full mb-7" id="especialidades">
                <h2 class="font-bold pb-2">1. Especialidades</h2>
                <div>
                    <button v-for="n in especialidades" :key="n"
                        type="button"
                        class="text-white bg-blue-700 hover:bg-blue-800  font-medium  text-sm px-4 py-2 mr-2 mb-2"
                        :aria-label="n.id"
                        @click="selectEspecialidad($event)">{{ n.nombre }}</button>
                </div>
            </div>

            <div class="mb-7" id="especialistas">
                <h2 class="font-bold pb-2">2. Especialistas</h2>
                <div>
                    <template v-if="especialistas.length > 0">
                        <button v-for="(n, index) in especialistas" :key="index"
                            type="button"
                            :class="['text-white bg-blue-700 hover:bg-blue-800 font-medium text-sm px-4 py-2 mr-2 mb-2', '']"
                            :aria-label="n.id"
                            @click="selectEspecialista($event)">{{ n.nombre }}</button>
                    </template>
                    <template v-else>
                        <p>Seleccione especialidad!</p>
                    </template>

                </div>
            </div>

            <div class="mb-7" id="disponible" ref="Disponible" style="display: none;">
                <h2 class="font-bold pb-2">3. Horario Disponible</h2>
                <div>
                    <form action="javascript:void(0);">
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
                            class="bg-blue-700 hover:bg-blue-800 text-white py-2 px-4 focus:outline-none focus:shadow-outline w-full"
                            @click="confirmSesion(event)">
                    </form>
                </div>
            </div>

            <!-- modal -->
            <PopUpPatientData/>

            <!-- <div class="w-full">
                <p class="mt-3 text-center text-gray-500 text-xs">
                    <a target="_blank" :href="authorURL">&copy;2023. All rights reserved. Developed by {{ authorName }}</a>
                </p>
            </div> -->
        </div>
    </div>
</template>
<style scoped>
    .selected{
        background-color: #1e429f;
    }
</style>