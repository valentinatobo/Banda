
class Instrumento():
    def __init__(self):
        self.imagen = "jpg"
        self.descripcion = ""
    def mostrar_instrumento(self):
        return "Instrumento"
    def retornar_info(self):
        return self.imagen, self.descripcion

class Guitarra(Instrumento):
    def __init__(self):
        self.imagen = "img/guitarra.jpg"
        self.descripcion = "Guitarra"
    def mostrar_instrumento(self):
        return "Guitarra"
    def retornar_info(self):
        return self.imagen, self.descripcion

class Organeta(Instrumento):
    def __init__(self):
        self.imagen = "img/organeta.jpg"
        self.descripcion = "Organeta"
    def mostrar_instrumento(self):
        return "Organeta"
    def retornar_info(self):
        return self.imagen, self.descripcion

class Bateria(Instrumento):
    def __init__(self):
        self.imagen = "img/bateria.jpg"
        self.descripcion = "Bateria"
    def mostrar_instrumento(self):
        return "Bateria"
    def retornar_info(self):
        return self.imagen, self.descripcion

class Saxofon(Instrumento):
    def __init__(self):
        self.imagen = "img/saxofon.jpg"
        self.descripcion = "Saxofon"
    def mostrar_instrumento(self):
        return "Saxofon"
    def retornar_info(self):
        return self.imagen, self.descripcion
    

class Violin(Instrumento):
    def __init__(self):
        self.imagen = "img/violin.jpg"
        self.descripcion = "Violin"
    def mostrar_instrumento(self):
        return "Violin"
    def retornar_info(self):
        return self.imagen, self.descripcion

