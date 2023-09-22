from instrumentos import *

class Principal():
    root = tk.Tk()
    root.title("Banda Aleatoria")

    canvas = tk.Canvas(root, width=900, height=500, bg="white")
    canvas.pack()

    instrumentos = [Guitarra(), Bajo(), Bateria(), Piano(), Saxofon()]
    imagenes = []

    for _ in range(5):
        inst = choice(instrumentos)
        imagenes.append(inst.imagen())

    x = 50
    separacion = 20

    for imagen in imagenes:
        canvas.create_image(x, 100, image=imagen, anchor=tk.NW)
        x += imagen.width() + separacion

    root.mainloop()
