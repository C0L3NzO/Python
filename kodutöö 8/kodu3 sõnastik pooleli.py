from random import randint

keel=str(input("Mis keelset sõna otsid? (inglise/eesti) "))
sõna=str(input("Millisele sõnale tõlget otsid? "))
f=open("sõnastik.txt")
kõik=f.readlines()
suurim=(len(kõik))
vähim=0
y=0
z=3
sõnakontroll=""
while True:
    x=randint(vähim,suurim-1)
    print(kõik[x])
    if str(kõik[2])<str(sõna[0]):
        vähim=x
    print(kõik[1])
    keel=str(input("enter"))
    if str(kõik[x][2])>str(sõna[0]):
        suurim=x
    if str(kõik[x][2])==str(sõna[0]):
        sõnakontroll+=kõik[x][0]
        while sõna!=sõnakontroll:
            if kõik[x+y][z]<sõna[z]:
                y-=1
            elif kõik[x+y][z]>sõna[z]:
                y+=1
            elif kõik[x+y][z]==sõna[z]:
                sõnakontroll+=kõik[x+y][z]
                z+=1
                print(sõnakontroll)