import socket
import random
import time
from select import select
import sys
from crc import bitstringABytes, bytesABitstring, crc_remainder, crc_check

msgFromClient       = ""
bytesToSend         = str.encode(msgFromClient)
serverAddressPort   = ("127.0.0.1", 20001)
bufferSize          = 1024
sent_packets        = 1
# Create a UDP socket at client side
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Se lee nombre desde el argumento del programa.
nombre = sys.argv[1]+'$'

# Send to server using created UDP socket
print("Intentando enviar")
#UDPClientSocket.sendto(str.encode("| Using Link Client 1: "), serverAddressPort)

# Genera la comunicacion entre estaciones
print("# Enviaremos: ", nombre)

while sent_packets!=len(nombre)+1:
    # Se envía una letra 
    num_packet = int(sent_packets).to_bytes(1,'little')
    letra = nombre[sent_packets-1].encode('ascii')

    paquete = num_packet+letra
    
    residuo = bitstringABytes(crc_remainder(bytesABitstring(paquete), '111010101'))
    paquete = paquete + residuo

    # Se simula corrupción de paquetes.
    if random.randrange(10) < 2:
        paquete = bytes(paquete[0]+1) + paquete[1:]
        
    UDPClientSocket.sendto(paquete, serverAddressPort)

    # Se espera 2 segs para recibir ACK
    ready = select([UDPClientSocket], [], [], 2)
    # Si se recibe ACK, se incrementa en 1 sent_packets
    if ready[0]:
        bytesAddressPair = UDPClientSocket.recvfrom(bufferSize)
        if bytesAddressPair[0][0]==sent_packets:
            sent_packets = sent_packets+1
            print("Se recibe ACK")
    else:
        print("Se reenvía paquete", sent_packets, "debido a timeout.")


print("# Texto enviado con éxito")
exit()