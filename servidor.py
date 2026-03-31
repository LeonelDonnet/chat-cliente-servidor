
import sqlite3
import socket
from datetime import datetime

# Configuración del servidor
HOST = '127.0.0.1'  # localhost
PORT = 5000

def iniciar_servidor():
    try:
        # Crear socket TCP/IP
        servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Asociar el socket a la dirección y puerto
        servidor.bind((HOST, PORT))

        # Escuchar conexiones entrantes
        servidor.listen()
        print(f"Servidor escuchando en {HOST}:{PORT}...")


        inicializar_db()

        while True:
            # Aceptar conexión de cliente
            conexion, direccion = servidor.accept()
            print(f"Conectado con {direccion}")

            # Recibir mensaje
            mensaje = conexion.recv(1024).decode()
            ip_cliente = direccion[0] 
            print(f"Mensaje recibido: {mensaje}")

            # Generar timestamp
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            guardar_mensaje(mensaje, timestamp, ip_cliente)

            # Respuesta al cliente
            respuesta = f"Mensaje recibido: {timestamp}"
            conexion.send(respuesta.encode())

            # Cerrar conexión
            conexion.close()

    except OSError:
        print("Error: el puerto 5000 ya está en uso.")
    except Exception as e:
        print(f"Error inesperado: {e}")

def inicializar_db():
    try:
        conexion = sqlite3.connect("chat.db")
        cursor = conexion.cursor()

        # Crear tabla si no existe
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS mensajes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                contenido TEXT,
                fecha_envio TEXT,
                ip_cliente TEXT
            )
        """)

        conexion.commit()
        conexion.close()

    except Exception as e:
        print(f"Error al inicializar la base de datos: {e}")

def guardar_mensaje(contenido, fecha, ip):
    try:
        conexion = sqlite3.connect("chat.db")
        cursor = conexion.cursor()

        cursor.execute("""
            INSERT INTO mensajes (contenido, fecha_envio, ip_cliente)
            VALUES (?, ?, ?)
        """, (contenido, fecha, ip))

        conexion.commit()
        conexion.close()

    except Exception as e:
        print(f"Error al guardar mensaje: {e}")


# Ejecutar servidor
iniciar_servidor()

