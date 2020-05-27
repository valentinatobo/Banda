from Instrumento import *
import random 
from random import choice

class Musico:

    def __init__(self):
        instrumentos = [Guitarra(),Bateria(),Organeta(),Saxofon(),Violin()]
        self.instrumento = choice(instrumentos)
    
    def mostrarInstrumento(self):
        return self.instrumento.mostrar_instrumento()

    def preparar_Instrumento(self):
        return "Preparando " + self.instrumento.mostrar_instrumento()

    def tocar_Instrumento(self):
        return "Tocando " + self.instrumento.mostrar_instrumento()
        