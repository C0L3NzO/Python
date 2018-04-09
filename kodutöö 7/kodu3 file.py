f=open(input("Sisesta faili nimi. "))

rida=f.readline()
see_mida_kirjutada=rida.strip()
print(see_mida_kirjutada)
ridasid=0
for rida in f:
    see_mida_kirjutada=rida.strip()
    print(see_mida_kirjutada)
    ridasid+=1
    if ridasid==(9):
        rida=f.readline()
        if rida=="":
            break
        enter=(input("----- jätkamiseks vajuta ENTER -----"))
        ridasid=0
        if enter!="":
            break
        see_mida_kirjutada=rida.strip()
        print(see_mida_kirjutada)
