import tkinter as tk
from random import choice
from PIL import Image, ImageTk

class Instrumento():
    def imagen(self):
        self.img = self.img.resize((150, 150))
        return ImageTk.PhotoImage(self.img)

class Guitarra(Instrumento):
    def imagen(self):
        self.img = Image.open("image/Guitarra.png")
        super().imagen()
        

class Bajo(Instrumento):
    def imagen(self):
        self.img = Image.open("image/Bajo.png")
        super().imagen()

class Bateria(Instrumento):
    def imagen(self):
        self.img = Image.open("image/Bateria.png")
        super().imagen()

class Piano(Instrumento):
    def imagen(self):
        self.img = Image.open("image/Piano.png")
        super().imagen()

class Saxofon(Instrumento):
    def imagen(self):
        self.img = Image.open("image/Saxofon.png")
        super().imagen()
    