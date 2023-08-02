from database import get_db

class Especialista:
    def __init__(self, id, nombre, especialidad_id):
        self.id = id
        self.nombre = nombre
        self.especialidad_id = especialidad_id

    @classmethod
    def all(cls):
        with get_db() as conn:
            cursor = conn.execute('SELECT * FROM especialistas')
            rows = cursor.fetchall()
            data = [{'id': row[0], 'nombre': row[1], 'especialidad_id': row[2]} for row in rows]
            return data

    @classmethod
    def by_especialidad(cls, especialidad_id):
        with get_db() as conn:
            cursor = conn.execute('SELECT * FROM especialistas WHERE especialidad_id = ?', (especialidad_id,))
            rows = cursor.fetchall()
            return [{'id': row[0], 'nombre': row[1]} for row in rows]