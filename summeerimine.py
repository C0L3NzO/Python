f=open("summeerimine.txt")
summa=0
while True:
    rida=f.readline()
    if rida=="":
        break
    arv=int(rida)
    summa=summa+arv
f.close()
print(summa)