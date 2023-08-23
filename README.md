# EsquemaComunicacion

Una empresa de celulares de gama alta quiere enviar sus archivos a una nueva sucursal que planean abrir proximamente, para ellos se creara un codigo que simule el envio 
y la recepción de un archivo de texto binario a través de un cable el cual llevara acabo los siguientes pasos que dan paso a la comunicación de la red.

El envio y recepción de archivos binarios atraves de un canal es esencial para , transmitir video , audio y la descarga de arvhisos de la empresa de celulares.

Para ello como primer paso el remitente abre el archivo de texto binario y lee los datos, despues el remitente divide los datos en paquetes de tamaño igual a la longitud del canal.
como siguiente paso en el remitente se puede agregar un encabezado a cada paquete que contiene información sobre el remitente, el destinatario, el tamaño del paquete y el tipo de dato enviado del archivo.
Posteriormente el remitente envia el paquete a través del canal utilizando una función de envío en ese momento el receptor recibe los paquetes del canal utilizando una función de recepción en ese momento 
el receptor desempaqueta los paquetes y los ensambla en datos utilizando una función de desempaquetado, por ultimo el  receptor escribe los datos en un archivo utilizando una función.

Podemos obervar que durante el proceso de envío y recepción de archivos de texto binario a través de un canal puede verse afectado por el ruido. El ruido logra corromper los paquetes, 
lo que puede hacer que el receptor no pueda desempaquetar los datos correctamente. Por lo tanto, el código también agrega ruido aleatorio a los paquetes antes de enviarlos.
Esto simula el ruido que puede ocurrir en un cable real y al recibir el paquete puede venir modificado por el ruido que paso durante su transmisión en el canal.

También consideramos que en el código también varía la velocidad de transmisión de los paquetes dependiendo del cable ya sea de fibra optica, cobre , entre otros.
Esto simula la diferencia en la velocidad de transmisión de diferentes tipos de cables , para ello lo que se puede hacer es Una forma es utilizar una función de retraso.
Una función de retraso es una función que retrasa la ejecución de código durante un período de tiempo especificado por ejemplo, una simulacion de la transmisión de un paquete a una velocidad de 100 kbps.
Otra forma de realizar puede ser utilizar una función de generación aleatoria para generar un número aleatorio que represente el tiempo que llevará transmitir el paquete.

Durante el programa se implementa un encabezado para cada paquete que contiene información sobre el remitente, el destinatario, el tamaño del paquete y el tipo de datos. El encabezado se utiliza para que 
los dispositivos de red puedan enviar los paquetes correctamente a sus destinos.El código también implementa una función para desempaquetar los datos que se envían en bits. 
