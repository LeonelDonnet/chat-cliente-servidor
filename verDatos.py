import sqlite3

conexion = sqlite3.connect("chat.db")
cursor = conexion.cursor()

cursor.execute("SELECT * FROM mensajes")
filas = cursor.fetchall()

for fila in filas:
    print(fila)

conexion.close()
