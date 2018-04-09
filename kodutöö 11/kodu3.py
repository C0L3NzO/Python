def seosta_lapsed_ja_vanemad():
    flaps=open("lapsed.txt")
    slaps={}
    fnimi=open("nimed.txt")
    snimi={}

    for i in fnimi:
        suva_list=i.strip().split()
        snimi[suva_list[0]]=suva_list[1]+" "+suva_list[2]

    for i in flaps:
        suva_list=i.strip().split()
        try:
            if slaps[suva_list[0]]>"":
                slaps[suva_list[0]]=snimi[slaps[suva_list[0]]]+", "+snimi[suva_list[1]]
        except: slaps[suva_list[0]]=suva_list[1]
    for i in slaps:
        try: slaps[i]=snimi[slaps[i]]
        except: slaps[i]=slaps[i]
    
    for i in slaps:
        print(snimi[i]+": "+slaps[i])
    
    flaps.close()
    fnimi.close()
seosta_lapsed_ja_vanemad()