from flask import Blueprint, jsonify, request
from models.especialidad import Especialidad
from models.especialista import Especialista
from models.sesion import Sesion

api_bp = Blueprint('api', __name__)

@api_bp.route('/especialidades', methods=['GET'])
def especialistas():
    """
    Example: http://localhost/api/especialidades

    Ruta para obtener todas las especialidades

    Returns:
    - JSON: Una lista de especialistas con la especialidad especificada.
    """
    especialidades = Especialidad.all()
    especialidades_json = [especialidad.to_json() for especialidad in especialidades]
    return jsonify(especialidades_json)

@api_bp.route('/especialistas', methods=['GET'])
def obtener_especialistas_por_especialidad_id():
    """
    Example: http://localhost/api/especialistas?especialidad=1

    Ruta para obtener especialistas por especialidad.

    Parámetros de consulta:
    - especialidad (int): El código de la especialidad para filtrar los especialistas.

    Returns:
    - JSON: Una lista de especialistas con la especialidad especificada.
    """
    especialidad_id = int(request.args.get('especialidad', 0))
    data = Especialista.by_especialidad(especialidad_id)
    json_data = [element.to_json() for element in data]
    return jsonify(json_data)

@api_bp.route('/sesiones', methods=['GET'])
def obtener_sesiones():
    """
    Example: http://localhost/api/sesiones
    http://localhost/api/sesiones?especialista_id=1&fecha_hora=2023-08-01%2010:00:00

    Ruta para obtener las sesiones.
    Ruta para obtener la disponibilidad del especialista

    Returns:
    - JSON: Una lista de sesiones.
    - JSON: True or False
    """
    especialista_id = request.args.get('especialista_id')
    fecha_hora = request.args.get('fecha_hora')
    if especialista_id and fecha_hora:
        data = Sesion.check_available_especialista(especialista_id, fecha_hora)
        json_data = data
    else:
        data = Sesion.all()
        json_data = [element.to_json() for element in data]
    return jsonify(json_data)