from math import pi
d=int(input("pitsa läbimõõt: "))
hind=float(input("pitsa hind: "))
pind=(pi*(d/2)**2)
print("Pitsa pindala on "+str(round(pind, 2))+" ruutsentimeetrit")
print("Iga ruutsentimeetri hind on "+str(round((hind/pind), 4))+" eurot")