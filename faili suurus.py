from os.path import getsize
def faili_suurus(fail):
    try:
        suurus=getsize(fail)
        return(suurus)
    except:
        return(0)
def teisenda(suurus):
    if suurus>=1024:
        arv=round(suurus/1024, 1)
        return (str(arv)+" KB")
    if suurus<1024:
        return str(suurus)
fail=str(input("Sisesta faili nimi või enter, et peatada. "))
while fail!="":
    print(str(teisenda(faili_suurus(fail)))+" B")
    fail=str(input("Sisesta faili nimi. "))

faili_suurus()