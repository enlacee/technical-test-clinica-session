const VITE_API_FLASK_ENDPOINT = import.meta.env.VITE_API_FLASK_ENDPOINT;
const BASE_URL = VITE_API_FLASK_ENDPOINT;

class SesionService {

    post(params = {}) {
        const data = params;
        const requestOptions = {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json', // Especificamos que estamos enviando datos en formato JSON
            },
            body: JSON.stringify(data), // Convertimos el objeto a una cadena JSON para enviarlo en el cuerpo
        };

        const url = BASE_URL + `/sesiones`;

        return fetch(url, requestOptions)
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

export default new SesionService();
