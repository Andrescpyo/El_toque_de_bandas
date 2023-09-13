from random import choice

class Musico():
    def __init__(self):
        self.musicos = ["Andres", "Juan", "Pepe", "Pedro", "David", "Alberto", "Ernesto", "Adrian", "Felipe"]

    def elegir_musico(self):
        return choice(self.musicos)
    



    
