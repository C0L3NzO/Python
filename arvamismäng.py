from random import randint
arv=randint(1, 999)
randEsimene=1
randTeine=999
arvamisteHulk = 0
input("Palun mõtle üks arv 1-st 999-ni. Kui valmis, vajuta enterit.")
print(arv)
while True:
    vastus = str(input("Kas oli < või >? Vajuta enter, kui õige arv. "))
    if vastus in ("<", ">", ""):
        if  vastus == "<":
            randEsimene = arv+1
            arv=randint(randEsimene, randTeine)
            print(arv)
            arvamisteHulk += 1
        elif vastus == ">":
            randTeine = arv-1
            arv=randint(randEsimene, randTeine)
            print(arv)
            arvamisteHulk += 1
        elif vastus == "":
            print("Hurraa! Arvasin "+str(arvamisteHulk)+" korraga õige vastuse.")
            break
