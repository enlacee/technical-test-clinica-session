import sqlite3
from database import get_db
from dataclasses import dataclass
import json

class Especialidad:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre

    @classmethod
    def all(cls):
        with get_db() as conn:
            cursor = conn.execute('SELECT * FROM especialidades')
            especialidades = cursor.fetchall()
            return [cls(*esp) for esp in especialidades]

    def to_json(self):
        return json.dumps(self.__dict__)