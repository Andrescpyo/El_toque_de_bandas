from random import choice

class Instrumento():
    def __init__(self):
        self.instrumentos=["Guitarra", "Bajo", "Bateria", "Piano"]

    def elegir_instrumento(self):
        return choice(self.instrumentos)
        
    def afinar_instrumento(self):
        pass

    def tocar_instrumento(self):
        pass

class Guitarra(Instrumento):
    def afinar_instrumento(self):
        return "Afinando Guitarra"
    
    def tocar_instrumento(self):
        return "Tocando Guitarra"

class Bajo(Instrumento):
    def afinar_instrumento(self):
        return "Afinando Bajo"

    def tocar_instrumento(self):
        return "Tocando Bajo"

class Bateria(Instrumento):
    def afinar_instrumento(self):
        return "Afinando Bateria"

    def tocar_instrumento(self):
        return "Tocando Bateria"

class Piano(Instrumento):
    def afinar_instrumento(self):
        return "Afinando Piano"
    
    def tocar_instrumento(self):
        return "Tocando Piano"