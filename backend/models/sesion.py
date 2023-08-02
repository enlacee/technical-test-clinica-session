from database import get_db

class Sesion:
    def __init__(self, id, especialista_id, paciente_nombre, paciente_data, fecha_hora):
        self.id = id
        self.especialista_id = especialista_id
        self.paciente_nombre = paciente_nombre
        self.paciente_data = paciente_data
        self.fecha_hora = fecha_hora

    def save(self):
        with get_db() as conn:
            conn.execute('INSERT INTO sesiones (especialista_id, paciente_nombre, paciente_data, fecha_hora) VALUES (?, ?, ?, ?)', (self.especialista_id, self.paciente_nombre, self.paciente_data, self.fecha_hora)).commit()

    @classmethod
    def all(cls):
        with get_db() as conn:
            query = """
                SELECT
                sesiones.id AS id,
                sesiones.paciente_nombre AS paciente_nombre,
                sesiones.fecha_hora AS fecha_hora,
                especialistas.nombre AS especialista_nombre,
                especialidades.nombre AS especialidad_nombre
                FROM sesiones
                INNER JOIN especialistas ON sesiones.especialista_id = especialistas.id
                INNER JOIN especialidades ON especialidades.id = especialistas.especialidad_id
                ORDER BY sesiones.id DESC
            """
            cursor = conn.execute(query)
            rows = cursor.fetchall()
            data = []
            for row in rows:
                diccionario = {
                    'id': row[0],
                    'paciente_nombre': row[1],
                    'fecha_hora': row[2],
                    'especialista_nombre': row[3],
                    'especialidad_nombre': row[4]
                }
                data.append(diccionario)
            return data

    @classmethod
    def check_available_especialista(cls, especialista_id, full_date):
        with get_db() as conn:
            query = "SELECT COUNT(*) FROM sesiones WHERE especialista_id = ? AND fecha_hora = ?"
            cursor = conn.execute(query, (especialista_id, f"{full_date}"))
            result = cursor.fetchone()
            return bool(result[0]) if result else False
