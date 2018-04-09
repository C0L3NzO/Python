from math import sqrt
x1=9
x2=13
y1=4
y2=7
def punktide_kaugus(a, b, c, d):
    kaugus=sqrt(((b-a)**2+(d-c)**2))
    return kaugus
kaugus1=punktide_kaugus(x1, x2, y1, y2)
kaugus2=