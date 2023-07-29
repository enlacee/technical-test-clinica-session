# SmartDoc - Aplicativo Web para la Gestión de Sesiones Clínicas

Este repositorio contiene un aplicativo web desarrollado para la gestión de sesiones de una clínica llamado SmartDoc. Los pacientes podrán acceder a información sobre las especialidades que ofrece la clínica, sus especialistas y los horarios disponibles por especialista.

## Instalación mediante Docker

Para ejecutar el proyecto, sigue los siguientes pasos:

1.- Asegúrate de tener Docker instalado en tu sistema.
2.- Clona este repositorio en tu máquina local.

```bash
    git clone https://github.com/tu_usuario/repositorio.git
```

3.- Navega a la carpeta del proyecto.

```bash
    cd repositorio
```

4.- Ejecuta el siguiente comando para construir y levantar los contenedores de Docker:

```bash
    docker-compose up --build
```

5.- Accede al aplicativo web desde tu navegador:

* Backend (Flask project): http://localhost:5000
* Frontend (Vue.js project): http://localhost:4000

## Estructura del Repositorio

El repositorio está estructurado de la siguiente manera:

* **backend**: Contiene el código del servidor desarrollado con Flask, que proporciona la lógica y las API para acceder a la información de la clínica.
* **frontend**: Incluye el código del cliente desarrollado con Vue.js, que presenta la interfaz de usuario y consume las API del backend para mostrar la información a los pacientes.

## Tecnologías Utilizadas

Backend: Flask (Python)
Frontend: Vue.js (JavaScript)
Base de datos: [SQLite]