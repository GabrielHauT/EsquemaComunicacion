import random

# Definimos los mensajes posibles
MENSAJES = ["Samsung S21", "Xiaomi 12Pro","Honor 70" ]

# Definimos la clase Fuente de información
class FuenteInformacion:
  def __init__(self, archivo_mensajes):
    self.archivo_mensajes = archivo_mensajes

  def generar_mensaje(self):
    with open(self.archivo_mensajes, "r") as archivo:
      return archivo.readline().strip()

# Definimos la clase Transmisor
class Transmisor:
  def __init__(self, probabilidad_ruido):
    self.probabilidad_ruido = probabilidad_ruido

  def transmitir_mensaje(self, mensaje):
    if self.probabilidad_ruido > 0.0 and random.random() < self.probabilidad_ruido:
      # Agrega ruido al mensaje
      mitad = len(mensaje) // 2
      mensaje = mensaje[:mitad] + "X" + mensaje[mitad:]

    return mensaje

# Definimos la clase Receptor
class Receptor:
  def __init__(self):
    pass

  def recibir_mensaje(self, mensaje):
    # Elimina el ruido del mensaje
    return mensaje.replace("X", "")

# Definimos la clase Destino de información
class DestinoInformacion:
  def __init__(self):
    pass

  def imprimir_mensaje(self, mensaje):
    print("El mensaje recibido es:", mensaje)

# Simulamos el esquema de comunicación
def main():
  # Inicializamos la semilla del generador de números aleatorios
  random.seed(time())

  # Creamos una fuente de información
  fuente_informacion = FuenteInformacion("mensajes.txt")

  # Creamos un transmisor
  transmisor = Transmisor(0.5)

  # Creamos un receptor
  receptor = Receptor()

  # Creamos un destino de información
  destino_informacion = DestinoInformacion()

  # Generamos un mensaje
  mensaje = fuente_informacion.generar_mensaje()

  # Transmitimos el mensaje
  mensaje = transmisor.transmitir_mensaje(mensaje)

  # Recibimos el mensaje
  mensaje = receptor.recibir_mensaje(mensaje)

  # Enviamos el mensaje al destino de información
  destino_informacion.imprimir_mensaje(mensaje)

if __name__ == "__main__":
  main()