from flask import Blueprint, jsonify
from models.especialidad import Especialidad

api_bp = Blueprint('api', __name__)

@api_bp.route('/')
def index():
    return {'data': 'some data'}

@api_bp.route('/especialidades', methods=['GET'])
def especialistas():
    especialidades = Especialidad.all()
    print("Especialidades:")
    # for especialidad in especialidades:
    #     print("-", especialidad)

    # Convertir la lista de objetos Especialidad a JSON y enviarla como respuesta
    especialidades_json = [especialidad.to_json() for especialidad in especialidades]
    return jsonify(especialidades_json)