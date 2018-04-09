x=0
summa=0
while x<999:
    x=x+1
    if x%3 == 0 or x%5 == 0:
        summa=summa+x
print(summa)