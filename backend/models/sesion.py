from database import get_db

from datetime import datetime

class Sesion:
    def __init__(self, id, especialista_id, paciente_nombre, paciente_data, fecha_hora):
        self.id = id
        self.especialista_id = especialista_id
        self.paciente_nombre = paciente_nombre
        self.paciente_data = paciente_data
        self.fecha_hora = fecha_hora

    def is_available(self):
        """
        Verifica si el especialista está disponible en la fecha y hora proporcionadas.

        Returns:
            bool: True si el especialista está disponible, False si no lo está.
        """
        with get_db() as conn:
            cursor = conn.execute('SELECT COUNT(*) FROM sesiones WHERE especialista_id = ? AND fecha_hora = ?',(self.especialista_id, self.fecha_hora))
            count = cursor.fetchone()[0]
            return count == 0

    def save(self):
        with get_db() as conn:
            conn.execute('INSERT INTO sesiones (especialista_id, paciente_nombre, paciente_data, fecha_hora) VALUES (?, ?, ?, ?)', (self.especialista_id, self.paciente_nombre, self.paciente_data, self.fecha_hora)).commit()

    @classmethod
    def all(cls):
        """Function printing python version."""
        with get_db() as conn:
            cursor = conn.execute('SELECT * FROM sesiones')
            sesiones = cursor.fetchall()
            return [cls(*ses) for ses in sesiones]

    @staticmethod
    def string_to_date(date_string):
        return datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S')

    @staticmethod
    def date_to_string(date):
        return date.strftime('%Y-%m-%d %H:%M:%S')
