from musicos import Musico
from instrumentos import *

u= Musico()
c = Instrumento()

print()
instrumentos = [Guitarra(), Bajo(), Bateria(), Piano(), Saxofon()]
banda =[]

for i in range(5):
    inst= c.elegir_instrumento(instrumentos)
    banda.append(inst)

    
for i in banda:
    musico = u.elegir_musico()
    print(f"{musico}: {i.afinar_instrumento()}")
    print(f"{musico}: {i.tocar_instrumento()}")
    print()

    


