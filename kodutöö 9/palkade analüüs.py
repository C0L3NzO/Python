f=open("palgad.txt")
info=[]
suurim_palk=0
keskmine_palk=0
keskmine_vanus_vähem=0
vähem_arv=0
keskmine_vanus_rohkem=0
rohkem_arv=0
x=0
for i in f:
    rida=i.strip().split(";")
    info.append(rida)
    
for i in info:
    if int(i[2])>int(suurim_palk):
        suurim_palk=i[2]
        töötaja_nimi=i[0]
    keskmine_palk+=int(i[2])
keskmine_palk//=len(info)

for i in info:
    if int(i[2])>keskmine_palk:
        x+=1
        keskmine_vanus_rohkem+=int(i[1])
        rohkem_arv+=1
    else:
        keskmine_vanus_vähem+=int(i[1])
        vähem_arv+=1
keskmine_vanus_rohkem//=rohkem_arv
keskmine_vanus_vähem//=vähem_arv

print("Kõige rohkem teenib "+töötaja_nimi+" - "+suurim_palk+".")
print("Keskmine palk on "+str(keskmine_palk)+".")
print("Keskmisest palgast rohkem teenib "+str(rohkem_arv)+" inimest.")
print("Keskmisest palgast rohkem teenivate inimeste keskmine vanus on "+str(keskmine_vanus_rohkem)+" ja vähem teenivate inimeste keskmine vanus on "+str(keskmine_vanus_vähem)+".")
f.close()
