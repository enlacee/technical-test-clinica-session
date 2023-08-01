import sqlite3
from database import get_db
from dataclasses import dataclass
import json

class Especialista:
    def __init__(self, id, nombre, especialidad_id):
        self.id = id
        self.nombre = nombre
        self.especialidad_id = especialidad_id

    @classmethod
    def all(cls):
        with get_db() as conn:
            cursor = conn.execute('SELECT * FROM especialistas')
            especialistas = cursor.fetchall()
            return [cls(*esp) for esp in especialistas]

    @classmethod
    def by_especialidad(cls, especialidad_id):
        with get_db() as conn:
            cursor = conn.execute('SELECT * FROM especialistas WHERE especialidad_id = ?', (especialidad_id,))
            especialistas = cursor.fetchall()
            return [cls(*esp) for esp in especialistas]

    def to_json(self):
        return json.dumps(self.__dict__)