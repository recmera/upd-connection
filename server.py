import socket
import time
import random
from crc import crc_remainder, crc_check, bytesABitstring, bitstringABytes


localIP     = "127.0.0.1"
localPort   = 20001
bufferSize  = 1024
msgFromServer       = "Datagram Acepted"
bytesToSend         = str.encode(msgFromServer)
actual_client = None
curr_name = ''
previous_client = None
previous_name = ''


# Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind to address and ip
UDPServerSocket.bind((localIP, localPort))
print("Link Available")


# Listen for incoming datagrams
while(True):

    
    # simulamos un tiempo de transmisión entre 0.5-1 segundos
    time.sleep(random.uniform(0.5,2))
    # Genera el 30%
    percent30 = random.randrange(10)

    # recibimos mensaje
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    
    #Evaluando CRC
    mensaje = bytesABitstring(bytesAddressPair[0])
    
    
    # mientras lo consideremos defectuoso por x motivo
    if percent30 < 3:
        # Informamos al cliente que el paquete está malo
        print("######## data loss ########")

    else:
        
        client_port = bytesAddressPair[1][1]
        
        # Si el servidor está disponible, se bloquea con el primer cliente 
        if actual_client == None:
            actual_client = client_port
        # Ignora los clientes mientras el servidor esté ocupado
        if actual_client != client_port:
            print("Cliente intenta comunicarse, pero el servidor no se encuentra disponible.")
        # Si el ultimo cliente no recibe el último ACK
        if actual_client == previous_client:
            UDPServerSocket.sendto(int(len(previous_name)).to_bytes(1,'little'), ("127.0.0.1", previous_client))
        # Si el cliente que envia un mensaje es el cliente actual
        if actual_client == client_port:
            if crc_check(mensaje[:16],'111010101', mensaje[16:]):

                letra = chr(bytesAddressPair[0][1])
                print(letra)
                num_packet = bytesAddressPair[0][0]
                # Si el numero de paquete coincide con el largo de la palabra almacenada
                if num_packet == len(curr_name)+1:
                    # Se envía un ACK con el numero de paquete recibido
                    curr_name = curr_name + letra
                    UDPServerSocket.sendto(int(len(curr_name)).to_bytes(1,'little'), bytesAddressPair[1])
                    # Si se recibe un signo $, entonces se envió la palabra
                    if letra == '$':
                        print("Nombre recibido.",curr_name)
                        previous_name = curr_name
                        previous_client = actual_client
                        actual_client = None
                        curr_name = ''
                else:
                    print("Paquete repetido. Se ignora.")
            else:
                print("El paquete está corrupto.")




        


    
  


    # Informamos al cliente que hemos recibido correctamente 
   