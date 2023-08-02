from flask import Flask
from dotenv import load_dotenv
from api.api import api_bp
from backoffice.backoffice import backoffice_bp
import database
import os

load_dotenv()
app = Flask(__name__)

# Función para habilitar CORS manualmente
def add_cors_headers(response):
    # Reemplaza '*' con el dominio de tu frontend Vue.js
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
    return response

@app.after_request
def after_request(response):
    return add_cors_headers(response)


# Código para manejar la base de datos
@app.teardown_appcontext
def teardown_db(exception):
    database.close_db()

# Inicializar la base de datos al arrancar la aplicación
with app.app_context():
    print("Creación de base de datos automático FIRST TIME")
    database.init_db()

app.register_blueprint(api_bp, url_prefix='/api')
app.register_blueprint(backoffice_bp, url_prefix='/')

if __name__ == '__main__':
    app.run(debug=True)