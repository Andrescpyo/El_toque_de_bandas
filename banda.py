from instrumentos import *

class Main():
    root = tk.Tk()
    root.title("Instrumentos Musicales")

    canvas = tk.Canvas(root, width=900, height=400)  # Ajusta el ancho y alto según tus necesidades
    canvas.pack()

    instrumentos = [Guitarra, Bajo, Bateria, Piano, Saxofon]
    x_spacing = 20
    images = []

    for _ in range(5):
        inst_class = choice(instrumentos)
        inst = inst_class()
        img = inst.imagen()
        images.append(img)
        canvas.create_text(x_spacing + 75, 10, text=f"Tocando {inst.__class__.__name__}", anchor=tk.N)
        canvas.create_image(x_spacing, 40, image=img, anchor=tk.NW)
        x_spacing += 150 + 20  # Ajusta el espaciado según tus necesidades

    root.mainloop()

