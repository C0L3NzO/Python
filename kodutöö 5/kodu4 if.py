päev=int(input("Sisesta päeva number. "))
kuu=int(input("Sisesta kuu number. "))
aasta=int(input("Sisesta aasta number. "))

def kuupäev_sõnena(p, k, a):
    päev=(str(p)+".")
    if k==1:
        kuu="jaanuar"
    if k==2:
        kuu="veebruar"
    if k==3:
        kuu="märts"
    if k==4:
        kuu="aprill"
    if k==5:
        kuu="mai"
    if k==6:
        kuu="juuni"
    if k==7:
        kuu="juuli"
    if k==8:
        kuu="august"
    if k==9:
        kuu="september"
    if k==10:
        kuu="oktoober"
    if k==11:
        kuu="november"
    if k==12:
        kuu="detsember"
    aasta=str(a)
    return(päev+" "+kuu+" "+aasta)
print(kuupäev_sõnena(päev, kuu, aasta))