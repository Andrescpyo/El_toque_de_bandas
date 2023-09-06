from musicos import Musico
from instrumentos import *

u= Musico()
c = Instrumento()

print("\n")
banda = []

for i in range(5):
    inst= c.elegir_instrumento()
    if inst == "Guitarra":
        banda.append(Guitarra())
    elif inst == "Bajo":
        banda.append(Bajo())
    elif inst == "Bateria":
        banda.append(Bateria())
    elif inst == "Piano":
        banda.append(Piano())
    
for i in banda:
    musico = u.elegir_musico()
    print(f"{musico}: {i.afinar_instrumento()}")
    print(f"{musico}: {i.tocar_instrumento()}")
    print()

    


