# CONEXIÓN UDP

###¿Qué es UDP?
El protocolo de datagramas de usuario, abreviado como UDP, es un protocolo que permite la transmisión sin conexión de datagramas en redes basadas en IP. Para obtener los servicios deseados en los hosts de destino, se basa en los puertos que están listados como uno de los campos principales en la cabecera UDP. Como muchos otros protocolos de red, UDP pertenece a la familia de protocolos de Internet, por lo que debe clasificarse en el nivel de transporte y, en consecuencia, se encuentra en una capa intermedia entre la capa de red y la capa de aplicación.

# Protocolo

Los clientes envían simultaneamente la letra inicial de su palabra al servidor junto con el numero de paquete (indice de la letra+1) más el residuo de CRC. 
El servidor se bloquea para trabajar únicamente con el primer cliente hasta recibir todo su nombre. Si es que otros clientes envían mensajes en ese estado, el servidor los ignorará.
La transferencia de un mensaje se produce cuando el servidor recibe el signo $.
El servidor verifica que el numero de paquete coincida con el largo del nombre almacenado actualmente y en el caso de que sea correcto envia un ACK al cliente indicando el numero de paquete.

El cliente envia una nueva letra unicamente si recibe el ACK del paquete anterior. Para el polinomio de CRC se utilizó el estandar CRC-8

# Método de ejecución
$ python servidor.py
$ python cliente.py nombre