import socket
import time
import json  # Para importat JSON

#Configuracion del socket UDP
UDP_IP = "0.0.0.0"
UDP_PORT = 4210 # Puerto de escucha del socket UDP puedo cambiar a 4211

# Inicializa socket UDP (socket.SOCK_DGRAM) por Internet (socket.AF_INET)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

sock.setblocking(True) # Bloquear (esperar) hasta recibir una interacción

while True:
    try:
        print()
        data, _ = sock.recvfrom(1024) # Tamaño máximo del mensaje
        decoded = data.decode().strip() #Decodifica mensaje y quita espacios
        valores = decoded.split(",") # Se quita si usamos JSON

        # Si el mensaje es un JSON, lo decodifica
        # valores = json.loads(decoded)

        x_porc = float(valores[0]) * 100
        y_porc = float(valores[1]) * 100
        print(f"x_porc = {x_porc} % , y_porc = {y_porc} %")
    except:
        print("Algo salio mal :( ")
        