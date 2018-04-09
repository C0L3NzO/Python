def paarisarvude_arv(x):
    paarisarvud=0
    for i in x:
        if i%2==0:
            paarisarvud+=1
    return paarisarvud
print(paarisarvude_arv([15,12, 2, 4, 6, 8]))