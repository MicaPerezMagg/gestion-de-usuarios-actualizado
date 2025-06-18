------------------------ Sistema de Gestión de Usuarios (Python + SQLite) -----------------------

Este proyecto es una aplicación de consola desarrollada para la EVIDENCIA 3, que permite gestionar usuarios diferenciando sus roles (Administrador y Usuario Estándar).

---------- Funciones principales

Registro de nuevos usuarios con validación de contraseña.
Inicio de sesión con verificación en base de datos.
Diferenciación de roles:
Usuario estándar: puede ver sus datos personales.
Administrador: puede ver todos los usuarios, cambiar roles y eliminar cuentas.
Control de acceso según rol.
Menú interactivo y mensajes informativos.
Gestión de datos a través de una base SQLite.
--------- Base de datos

Se utiliza SQLite para almacenar los datos de los usuarios y los roles.

Tablas creadas: Usuario,Rol-------------------------------
Scripts SQL incluidos:
-- Creación de la base de datos
CREATE DATABASE IF NOT EXISTS sistema_usuarios;
USE sistema_usuarios;

-- Tabla de usuarios
CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(100) NOT NULL UNIQUE,
    nombre VARCHAR(100) NOT NULL,
    password VARCHAR(255) NOT NULL,
    rol ENUM('admin', 'usuario') NOT NULL
);

-- Usuarios iniciales
INSERT INTO usuarios (email, nombre, password, rol) VALUES
('admin@correo.com', 'Administrador', 'Admin123', 'admin'),
('usuario@correo.com', 'Usuario Normal', 'Usuario123', 'usuario');
-----------------------------------------------------------------------
Consultas CRUD para usuarios.
Archivo usuarios.dbincluido para pruebas.
-------- Estructura del código

Modularidad con clases: Usuario, UsuarioEstandar, Administrador.
Uso de Programación Orientada a Objetos.
Validaciones y separación de funcionalidades por rol.
-------- Herramientas utilizadas

Python 3.x
SQLite
Git y GitHub
------ Realizado por:

ALUMNA: Carla Micaela Pérez Maggetti
ENLACE al repositorio: https://github.com/MicaPerezMagg/sistema-de-gestion-usuarios
Proyecto realizado para la carrera Desarrollo Web y Aplicaciones Digitales del ISPC.

