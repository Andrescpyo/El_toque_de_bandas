from random import choice
import tkinter as tk
from tkinter import ttk


class Instrumento():
    def elegir_instrumento(self, instrumentos):
        return choice(instrumentos)
        
    def afinar_instrumento(self):
        pass

    def tocar_instrumento(self):
        pass

    def imagen(self):
        pass
        

class Guitarra(Instrumento):
    def afinar_instrumento(self):
        return "Afinando Guitarra"
    
    def tocar_instrumento(self):
        return "Tocando Guitarra"

    def imagen(self):
        return "AfinarGuitarra.png"      

class Bajo(Instrumento):
    def afinar_instrumento(self):
        return "Afinando Bajo"

    def tocar_instrumento(self):
        return "Tocando Bajo"
    
    def imagen(self):
        return "Bajo.png"

class Bateria(Instrumento):
    def afinar_instrumento(self):
        return "Afinando Bateria"

    def tocar_instrumento(self):
        return "Tocando Bateria"

    def imagen(self):
        return "Bateria.png"
        

class Piano(Instrumento):
    def afinar_instrumento(self):
        return "Afinando Piano"
    
    def tocar_instrumento(self):
        return "Tocando Piano"
    
    def imagen(self):
        return "Piano.png"
    
class Saxofon(Instrumento):
    def afinar_instrumento(self):
        return "Afinando Saxofón"

    def tocar_instrumento(self):
        return "Tocando Saxofón"
    
    def imagen(self):
        return "Saxofon.png"
    