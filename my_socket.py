import socket
import time

#Configuracion del socket UDP
UDP_IP = "0.0.0.0"
UDP_PORT = 4210

# Inicializa socket UDP (socket.SOCK_DGRAM) por Internet (socket.AF_INET)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

sock.setblocking(True) # Bloquear (esperar) hasta recibir una interacción

while True:
  try:
    print()
    data, addr = sock.recvfrom(1024) # Tamaño máximo del mensaje
    decoded = data.decode().strip() #Decodifica mensaje y quita espacios
    # valor = decoded
    # print(f"valor = {valor}")
    print(f"\n[Cliente {addr[0]}: {addr[1]}] -> {decoded}")
  except:
    print("Algo salio mal :( ")