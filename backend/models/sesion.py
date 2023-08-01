import sqlite3
from database import get_db
from dataclasses import dataclass
import json
from datetime import datetime

class Sesion:
    def __init__(self, id, especialista_id, paciente_nombre, paciente_data, fecha_hora):
        self.id = id
        self.especialista_id = especialista_id
        self.paciente_nombre = paciente_nombre
        self.paciente_data = paciente_data
        self.fecha_hora = fecha_hora

    # def save(self):
    #     with get_db() as conn:
    #         conn.execute('INSERT INTO sesiones (especialista_id, paciente_nombre, paciente_data, fecha_hora) VALUES (?, ?, ?, ?)', (self.especialista_id, self.paciente_nombre, self.paciente_data, self.fecha_hora)).commit()

    @classmethod
    def all(cls):
        with get_db() as conn:
            cursor = conn.execute('SELECT * FROM sesiones')
            sesiones = cursor.fetchall()
            return [cls(*ses) for ses in sesiones]

    @classmethod
    def check_available_especialista(cls, especialista_id, full_date):
        with get_db() as conn:
            query = "SELECT COUNT(*) FROM sesiones WHERE especialista_id = ? AND fecha_hora = ?"
            cursor = conn.execute(query, (especialista_id, f"{full_date}"))
            result = cursor.fetchone()
            return bool(result[0]) if result else False

    def to_json(self):
        return json.dumps(self.__dict__)
