import tkinter as tk
from random import choice
from PIL import Image, ImageTk

class Instrumento():
    def imagen(self):
        pass

class Guitarra(Instrumento):
    def imagen(self):
        img = Image.open("image/Guitarra.png")
        img = img.resize((150, 150))
        return ImageTk.PhotoImage(img)

class Bajo(Instrumento):
    def imagen(self):
        img = Image.open("image/Bajo.png")
        img = img.resize((150, 150))
        return ImageTk.PhotoImage(img)

class Bateria(Instrumento):
    def imagen(self):
        img = Image.open("image/Bateria.png")
        img = img.resize((150, 150))
        return ImageTk.PhotoImage(img)

class Piano(Instrumento):
    def imagen(self):
        img = Image.open("image/Piano.png")
        img = img.resize((150, 150))
        return ImageTk.PhotoImage(img)

class Saxofon(Instrumento):
    def imagen(self):
        img = Image.open("image/Saxofon.png")
        img = img.resize((150, 150))
        return ImageTk.PhotoImage(img)

    