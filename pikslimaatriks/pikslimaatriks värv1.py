from pixboard import *
from math import sin, radians, pi, sqrt

pilt = load_color("varvipilt.gif")

kõrgus=len(pilt)
laius=len(pilt[0])

for y in range(kõrgus):
    for x in range(laius):
        heledus=pilt[y][x]
        uus_heledus=(heledus[1], heledus[0], heledus[1])
        pilt[y][x]=uus_heledus

show(pilt)