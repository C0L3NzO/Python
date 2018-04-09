def korrasta_kuupäev(kuupäev):
    versioon_a=0
    try:
        aastaint=int(kuupäev[6]+kuupäev[7]+kuupäev[8]+kuupäev[9])
        versioon_a=1
    except:
        aastaint=int(kuupäev[0]+kuupäev[1]+kuupäev[2]+kuupäev[3])

    if versioon_a==1:
        kuustr=str(kuupäev[3]+kuupäev[4])
    else:
        kuustr=str(kuupäev[5]+kuupäev[6])

    if versioon_a==1:
        päevint=int(kuupäev[0]+kuupäev[1])
    else:
        päevint=int(kuupäev[8]+kuupäev[9])

    if kuustr[0]==0:
        kuuint=int(kuustr[1])
    else:
        kuuint=int(kuustr)

    if kuuint==1:
        kuu="jaanuar"
    if kuuint==2:
        kuu="veebruar"
    if kuuint==3:
        kuu="märts"
    if kuuint==4:
        kuu="aprill"
    if kuuint==5:
        kuu="mai"
    if kuuint==6:
        kuu="juuni"
    if kuuint==7:
        kuu="juuli"
    if kuuint==8:
        kuu="august"
    if kuuint==9:
        kuu="september"
    if kuuint==10:
        kuu="oktoober"
    if kuuint==11:
        kuu="november"
    if kuuint==12:
        kuu="detsember"
        
    aasta=str(aastaint)
    
    päev=str(päevint)
    
    return(päev+ ". " +kuu+ " " +aasta)

print(korrasta_kuupäev("2017.10.11"))


