def isikukoodi_osad(kood):
    sünnikoht=""
    haigla="pole"
    esimene=kood[0]
    
    if esimene=="2":
        aasta1="18"
        sugu="Naine"
        
    if esimene=="4":
        aasta1="19"
        sugu="Naine"
        
    if esimene=="6":
        aasta1="20"
        sugu="Naine"
        
    if esimene=="1":
        aasta1="18"
        sugu="Mees"
        
    if esimene=="3":
        aasta1="19"
        sugu="Mees"
        
    if esimene=="5":
        aasta1="20"
        sugu="Mees"
    
    aasta2=int(kood[1]+kood[2])
    if aasta1== "20" and aasta2<=13 or aasta1=="19":
        haigla="on"
    
    kuu=str(kood[3]+kood[4])

    päev=str(kood[5]+kood[6])

    if haigla=="on":
        number3=(str(kood[7]+kood[8]+kood[9]))
        arv=int(number3)
                
        if arv >= 1 and arv <= 10:
            sünnikoht="Kuressaare Haigla"
        if arv >= 11 and arv <= 19:
            sünnikoht="Tartu Ülikooli Naistekliinik, Tartu või Tartumaa"
        if arv >= 21 and arv <= 220:
            sünnikoht="Ida-Tallinna Keskhaigla, Pelgulinna sünnitusmaja, Hiiumaa, Keila, Rapla haigla või Loksa haigla"
        if arv >= 221 and arv <= 270:
            sünnikoht="Ida-Viru Keskhaigla (Kohtla-Järve, endine Jõhvi)"
        if arv >=271 and arv <= 370:
            sünnikoht="Maarjamõisa Kliinikum (Tartu) või Jõgeva Haigla"
        if arv >=371 and arv <= 420:
            sünnikoht="Narva Haigla"
        if arv >=421 and arv <= 470:
            sünnikoht="Pärnu Haigla"
        if arv >=471 and arv <= 490:
            sünnikoht="Pelgulinna Sünnitusmaja (Tallinn) või Haapsalu haigla"
        if arv >=491 and arv <= 520:
            sünnikoht="Järvamaa Haigla (Paide)"
        if arv >=521 and arv <= 570:
            sünnikoht="Rakvere või Tapa haigla"
        if arv >=571 and arv <= 600:
            sünnikoht="Valga Haigla"
        if arv >=601 and arv <= 650:
            sünnikoht="Viljandi Haigla"
        if arv >=651 and arv <= 710:
            sünnikoht="Lõuna-Eesti Haigla (Võru), Põlva Haigla"
    aasta2=str(aasta2)
    print("Lugesin välja järgneva info:")
    print("  Sugu: "+ sugu)
    print("  Sünnikuupäev: "+ päev+"."+kuu+"."+aasta1+aasta2)
    print("  Sünnikoht: " +sünnikoht)
isikukoodi_osad("36807043445")