from flask import Blueprint, jsonify, request
from models.especialidad import Especialidad
from models.especialista import Especialista
from models.sesion import Sesion

api_bp = Blueprint('api', __name__)

@api_bp.route('/especialidades', methods=['GET'])
def especialistas():
    """
    Example: /especialidades

    Ruta para obtener todas las especialidades

    Returns:
    - JSON: Una lista de especialistas con la especialidad especificada.
    """
    result = Especialidad.all()
    return jsonify(result)

@api_bp.route('/especialistas', methods=['GET'])
def obtener_especialistas_por_especialidad_id():
    """
    Example: /especialistas?especialidad=1

    Ruta para obtener especialistas por especialidad.

    Parámetros de consulta:
    - especialidad (int): El código de la especialidad para filtrar los especialistas.

    Returns:
    - JSON: Una lista de especialistas con la especialidad especificada.
    """
    especialidad_id = int(request.args.get('especialidad', 0))
    data = Especialista.by_especialidad(especialidad_id)
    return jsonify(data)

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
        json_data = Sesion.all()
    return jsonify(json_data)

@api_bp.route('/sesiones', methods=['POST'])
def registrar_sesion():
    """
    Example: http://localhost/api/sesiones

    Ruta para registrar una nueva sesion

    Returns:
    - JSON: informacion del registro o error message.
    """
    data = request.get_json()
    id = '' #data.get('id')
    especialista_id = data.get('especialista_id')
    paciente_nombre = data.get('paciente_nombre')
    paciente_data = data.get('paciente_data')
    fecha_hora = data.get('fecha_hora')

    try:
        # Verificar que los datos necesarios estén presentes en la solicitud
        if not id or not especialista_id or not paciente_nombre or not paciente_data or not fecha_hora:
            return jsonify({"error": "Faltan datos en la solicitud"}), 400

        nueva_sesion = Sesion(id=id, especialista_id=especialista_id, paciente_nombre=paciente_nombre, paciente_data=paciente_data, fecha_hora=fecha_hora)
        nueva_sesion.save()

        return jsonify({"mensaje": "Sesión registrada exitosamente"}), 201
    except Exception as e:
        return jsonify({"error": "Error al registrar la sesión", "detalle": str(e)}), 500