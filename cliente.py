import socket

HOST = '127.0.0.1'
PORT = 5000

def iniciar_cliente():
    while True:
        mensaje = input("Escribí un mensaje (o 'exito' para salir): ")

        if mensaje.lower() == "exito":
            print("Cerrando cliente...")
            break

        try:
            # Crear socket
            cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            # Conectarse al servidor
            cliente.connect((HOST, PORT))

            # Enviar mensaje
            cliente.send(mensaje.encode())

            # Recibir respuesta
            respuesta = cliente.recv(1024).decode()
            print(f"Servidor responde: {respuesta}")

            # Cerrar conexión
            cliente.close()

        except ConnectionRefusedError:
            print("Error: el servidor no está activo.")
        except Exception as e:
            print(f"Error inesperado: {e}")

# Ejecutar cliente
iniciar_cliente()
