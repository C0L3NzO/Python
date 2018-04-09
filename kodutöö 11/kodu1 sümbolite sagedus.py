def sümbolite_sagedus(sõne):
    sõnastik={}
    for i in sõne:
        try:
            if sõnastik[i]>0:
                x=sõnastik[i]
                sõnastik[i]=x+1
        except: sõnastik[i]=1
    print(sõnastik)
def erinevad_sümbolid(sõne):
    hulk=set()
    for i in sõne:
        hulk.add(i)
    print(hulk)

sümbolite_sagedus("Vanapagana tagavara rahapada")