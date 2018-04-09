def erinevad_sõnad(sõne):
    järjend=sõne.split()
    sõnad=[]
    x=0
    y=1
    lower=järjend[0].lower()
    sõnad.append(lower)
    for i in järjend:
        if (sõnad[x]).lower!=(järjend[y]).lower and y<=len(järjend):
            sõnad.append(i)
            x+=1
        y+=1
    return sõnad
print(erinevad_sõnad("Tere tere tere tort kare Kare"))
        
            