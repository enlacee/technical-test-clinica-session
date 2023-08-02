const VITE_API_FLASK_ENDPOINT = import.meta.env.VITE_API_FLASK_ENDPOINT;
const BASE_URL = VITE_API_FLASK_ENDPOINT;

class EspecialistaService {

    /**
     * Obtener todas las especialidades
     *
     * @returns {Promise<object>}
     */
    get(data = {}) {
        const { especialidad } = data; // {a:111, b:222}; Destructuring assignment
        const url = BASE_URL + `/especialistas?especialidad=${especialidad}`;

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

export default new EspecialistaService();
