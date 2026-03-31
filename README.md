# Chat Cliente-Servidor con Python

## Descripción
En este proyecto implemente un sistema de chat básico cliente-servidor utilizando sockets en Python.  
El servidor recibe mensajes de múltiples clientes, los almacena en una base de datos SQLite y responde con un timestamp.

## Tecnologías utilizadas
- Python 3
- Sockets (TCP/IP)
- SQLite

## Estructura
- servidor.py → El servidor recibe y almacena mensajes
- cliente.py → Cliente que envía mensajes
- verDatos.py → Script para visualizar los datos almacenados

## Cómo ejecutar

### 1. Iniciar servidor
```bash
python servidor.py

