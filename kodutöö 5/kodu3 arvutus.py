from math import sqrt
x1=int(input("Mis on esimese punkti x-koordinaat? "))
y1=int(input("Mis on esimese punkti y-koordinaat? "))
x2=int(input("Mis on teise punkti x-koordinaat? "))
y2=int(input("Mis on teise punkti y-koordinaat? "))
x3=int(input("Mis on kolmanda punkti x-koordinaat? "))
y3=int(input("Mis on kolmanda punkti y-koordinaat? "))

def punktide_kaugus(a, b, c, d):
    kaugus=sqrt(((b-a)**2+(d-c)**2))
    return kaugus

kaugus1=punktide_kaugus(x1, x2, y1, y2)
kaugus2=punktide_kaugus(x1, x3, y1, y3)
kaugus3=punktide_kaugus(x2, x3, y2, y3)

if kaugus1<kaugus2 and kaugus1<kaugus3:
    vastus1="esimene"
    vastus2="teine"
elif kaugus2<kaugus1 and kaugus2<kaugus3:
    vastus1="esimene"
    vastus2="kolmas"
elif kaugus3<kaugus1 and kaugus3<kaugus2:
    vastus1="teine"
    vastus2="kolmas"

print("Omavahel lähimad punktid on "+ vastus1 +" ja "+ vastus2 +".")