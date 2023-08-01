from flask import Flask
from api.api import api_bp
from backoffice.backoffice import backoffice_bp
import database

app = Flask(__name__)

app.register_blueprint(api_bp, url_prefix='/api')
app.register_blueprint(backoffice_bp, url_prefix='/')

# Código para manejar la base de datos
@app.teardown_appcontext
def teardown_db(exception):
    database.close_db()

# Inicializar la base de datos al arrancar la aplicación
with app.app_context():
    print("Creación de base de datos automático FIRST TIME")
    database.init_db()

if __name__ == '__main__':
    app.run(debug=True)