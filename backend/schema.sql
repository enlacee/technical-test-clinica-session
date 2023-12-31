-- Crear tabla para especialidades
CREATE TABLE especialidades (
    id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL
);

-- Insertar datos de prueba en la tabla especialidades
INSERT INTO especialidades (nombre) VALUES
    ('Cardiología'),
    ('Dermatología'),
    ('Pediatría'),
    ('Oftalmología');

-- Crear tabla para especialistas
CREATE TABLE especialistas (
    id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    especialidad_id INTEGER NOT NULL,
    FOREIGN KEY (especialidad_id) REFERENCES especialidades(id)
);

-- Insertar datos de prueba en la tabla especialistas
INSERT INTO especialistas (nombre, especialidad_id) VALUES
    ('Dr. Juan Pérez', 1),
    ('Dra. María Gómez', 2),
    ('Dr. Luis Ramírez', 3),
    ('Dra. Ana Martínez', 4),
    ('Dr. JoseMaria Argueda', 1),
    ('Dr. Roberto Sano', 1),
    ('Dra. Cristina Roble', 1);

-- Crear tabla para sesiones
CREATE TABLE sesiones (
    id INTEGER PRIMARY KEY,
    especialista_id INTEGER NOT NULL,
    paciente_nombre TEXT NOT NULL,
    paciente_data JSON NOT NULL,
    fecha_hora TEXT NOT NULL,
    FOREIGN KEY (especialista_id) REFERENCES especialistas(id)
);

-- Insertar datos de prueba en la tabla sesiones
INSERT INTO sesiones (especialista_id, paciente_nombre, paciente_data, fecha_hora) VALUES
    (1, 'Percy Lopez', '{"nombre": "Percy", "apellido": "Lopez", "correo": "percy@example.com", "telefono": "1234567890"}', '2023-08-01 10:00:00'),
    (2, 'Mario Rojas', '{"nombre": "Mario", "apellido": "Rojas", "correo": "mario@example.com", "telefono": "9876543210"}', '2023-08-02 15:00:00'),
    (3, 'Carlos Lora', '{"nombre": "Carlos", "apellido": "Lora", "correo": "carlos@example.com", "telefono": "5555555555"}', '2023-08-03 10:00:00');

