valuutad={}
kurrside_sõnastik={}
ajutinesõn={}
f=open("valuutakursid.txt")
for i in f:
    ajutine=i.split("\t")
    valuutad[ajutine[0]]=(ajutine[2].strip())
valuutad["EUR"]=1.0
for i in valuutad:
    for j in valuutad:
        if i!=j:
            ajutinesõn[j]=round(float(valuutad[i])/float(valuutad[j]), 4)
    kurrside_sõnastik[i]=ajutinesõn
print(kurrside_sõnastik)
lähte=str(input("Lähtevaluuta lühend: "))
siht=str(input("Sihtvaluuta lühend: "))
hulk=str(input("Raha hulk: "))
for i in valuutad:
    if lähte==i:
        a=valuutad[i]
    if siht==i:
        b=valuutad[i]
print(hulk+" "+lähte+" eest saab "+str(round(float(b)/float(a)*float(hulk), 4))+" "+siht+".")
