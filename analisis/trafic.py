import pyshark
import csv
import time

# Definir una función de callback para procesar cada paquete capturado
def packet_callback(pkt):
    packet_info = {
        "No. de paquete": pkt.number,
        "Time": pkt.sniff_time,
        "Source": pkt.ip.src if 'IP' in pkt else '-',
        "Port Source": pkt.tcp.srcport if 'TCP' in pkt else '-',
        "Destination": pkt.ip.dst if 'IP' in pkt else '-',
        "Port Destination": pkt.tcp.dstport if 'TCP' in pkt else '-',
        "Protocol": pkt.transport_layer,
        "Length": pkt.length,
        "Info": pkt.info if hasattr(pkt, 'info') else '-',
        "Flag": pkt.flags if hasattr(pkt, 'flags') else '-'
    }
    write_to_csv(packet_info)

# Función para escribir la información del paquete en un archivo CSV
def write_to_csv(packet_info):
    with open('captura_trafico.csv', mode='a', newline='') as file:
        fieldnames = ["No. de paquete", "Time", "Source", "Port Source", "Destination", "Port Destination", "Protocol", "Length", "Info", "Flag"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        
        if file.tell() == 0:
            writer.writeheader()
        
        writer.writerow(packet_info)

# Capturar tráfico de red en tiempo real en la interfaz de red especificada
capture = pyshark.LiveCapture(interface='Wi-fi')

# Tiempo de captura en segundos 
capture_duration = 420

start_time = time.time()

# Ejecutar la captura con la función de callback definida
for pkt in capture.sniff_continuously(packet_count=0):
    packet_callback(pkt)
    # Verificar si ha transcrrido el tiempo
    if time.time() - start_time >= capture_duration:
        print('listo termine.')
        break
