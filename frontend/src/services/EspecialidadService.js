const VITE_API_FLASK_ENDPOINT = import.meta.env.VITE_API_FLASK_ENDPOINT;
const BASE_URL = VITE_API_FLASK_ENDPOINT;

class EspecialidadService {

    /**
     * Obtener todas las especialidades
     *
     * @returns {Promise<object>}
     */
    get() {
        const url = BASE_URL + `/especialidades`;

        return fetch(url, { method: 'GET' })
        .then(response => {
            if (!response.ok) {
                throw new Error('Error al obtener los datos');
            }
            return response.json();
        })
        .catch(error => {
            console.error(error);
            throw error;
        });
    }
}

export default new EspecialidadService();
