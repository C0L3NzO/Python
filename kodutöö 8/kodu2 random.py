from random import randint
def lause():
    while True:
        f1=open("alus.txt")
        f2=open("öeldis.txt")
        f3=open("sihitis.txt")
        alus=f1.readlines()
        öeldis=f2.readlines()
        sihitis=f3.readlines()
        n1=randint(0,9)
        n2=randint(0,9)
        n3=randint(0,9)
        print((alus[n1].strip())+" "+(öeldis[n2].strip())+" "+(sihitis[n3].strip()))
        enter=str(input("Vajuta enter"))
        if enter!="":
            break
        
    f1.close()
    f2.close()
    f3.close()
lause()