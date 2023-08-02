from database import get_db

class Especialidad:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre

    @classmethod
    def all(cls):
        with get_db() as conn:
            cursor = conn.execute('SELECT * FROM especialidades')
            rows = cursor.fetchall()
            data = [{'id': row[0], 'nombre': row[1]} for row in rows]
            return data