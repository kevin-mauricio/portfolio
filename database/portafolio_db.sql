DROP DATABASE IF EXISTS portafolio_db;
CREATE DATABASE portafolio_db;
USE portafolio_db;

CREATE TABLE mensajes(
    id_mensaje INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    nombres VARCHAR(40),
    correo VARCHAR(100),
    asunto VARCHAR(80),
    mensaje TEXT,
    fecha_envio DATETIME DEFAULT CURRENT_TIMESTAMP
);