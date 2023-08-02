from flask import Blueprint, render_template
import requests

backoffice_bp = Blueprint('backoffice', __name__)

@backoffice_bp.route('/')
def backoffice():
    url_base = 'http://localhost:5000/api'
    url = f"{url_base}/sesiones"
    response = requests.get(url)
    if response.status_code == 200:
        sesiones = response.json()
        return render_template('sesiones.html', sesiones=sesiones)
    else:
        return f"Error al obtener las sesiones. Código de estado: {response.status_code}"