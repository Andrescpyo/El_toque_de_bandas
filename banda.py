from musicos import Musico
from instrumentos import *

class Ventana():
    def __init__(self, root, imagen):
        self.root = root
        self.root.title("Ventana con Imagen")
        self.imagen = tk.PhotoImage(file = imagen)
        self.imagen = self.imagen.subsample(2, 2)
        self.label_imagen = tk.Label(root, image=self.imagen)
        self.label_imagen.pack()

c = Instrumento()
instrumentos = [Guitarra(), Bajo(), Bateria(), Piano(), Saxofon()]
banda =[]
root = tk.Tk()
imagenes= []

for i in range(5):
    inst= c.elegir_instrumento(instrumentos)
    banda.append(inst)

for i in banda:
    imagenes.append(i.imagen())

for i in imagenes:
    ventana= Ventana(root, i)

root.mainloop()

    

