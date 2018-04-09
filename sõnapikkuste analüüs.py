def sõnapikkused(fail):
    x=1
    faili_sisu=[]
    pikkused=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    f=open(fail)
    for i in f:
        temp=i.split()
        faili_sisu+=temp
    for i in faili_sisu:
        if len(i)<15:
            pikkused[len(i)-1]+=1
        else: pikkused[14]+=1
    for i in pikkused:
        if x>15 and pikkused[14]!=0: print("15 või rohkema tähega sõnu oli failis "+str(pikkused[14])+".")
        if i>0 and x<15: print(str(x)+" tähe pikkuseid sõnu oli failis "+str(i)+".")
        x+=1
    return
fail=(input("Mis on faili nimi? "))
sõnapikkused(fail)