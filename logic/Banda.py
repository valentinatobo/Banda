from Musico import Musico
import random 

class Banda:
   def __init__(self):
      #Arreglo de musicos que conforman la banda
      self.musicos = []
      self.musicoscompletos = []
 
   def agregarMusico(self):
      #Crear musico
      self.musicos.append(Musico())
      

   def construir_Banda(self):
      #Repetir el numero de veces necesario para que exista todos los musicos de la banda (cantidad)
      cantidad = random.randint(5, 10)
      for i in range (0, cantidad):
         #agregar musico con el metodo PROPIO(self)
         self.agregarMusico()

   def prepararBanda(self):
      print("*********** PREPARANDO BANDA ***********")
      for x in range(0,len(self.musicos)):
         print(self.musicos[x].preparar_Instrumento())
         
   def tocarBanda(self):
      print("*********** BANDA TOCANDO ***********")
      for x in range(0,len(self.musicos)):
         print(self.musicos[x].tocar_Instrumento())
         
   
