#võtab ühe rea failist (faili nimeks panna näiteks t.txt)
nimi=str(input("Sisesta faili nimi: "))
arv=int(input("Sisesta positiivne täisarv: "))
x=0
f=open(nimi)
while x<arv:
    rida=f.readline()
    x=x+1
print(rida[0])
f.close()