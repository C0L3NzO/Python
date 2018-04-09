from pykkar import *
laius=0
kõrgus=0
x=0
y=0

def maailm(suurus, sõna):
    while True:
        try:
            suurus=int(input("Sisesta maailma "+ sõna + ": "))
            return suurus
        except:
            print("Vigane sisend! Proovime uuesti ...")

def koordinaat(täht, küsitav, suurus):
    while True:
        try:
            täht=int(input("Sisesta Pykkari positsiooni "+ küsitav +"-koordinaat: "))
            if täht < 2:
                print("Liiga väike! Proovime uuesti ...")
            elif täht > suurus-1:
                print("Liiga suur! Proovime uuesti ...")
            else:
                return täht
        except:
            print("Vigane sisend! Proovime uuesti ...")

laius=maailm(laius, "laius")
kõrgus=maailm(kõrgus, "kõrgus")         #siin toimub maailma andmete küsimine funktsioonidega
x=koordinaat(x, "x", laius)
y=koordinaat(y, "y", kõrgus)

while True:
        try:
            suund=str(input("Sisesta Pykkari suund (<, ^, v, >): "))        #ja siin suuna küsimine
            if suund=="<" or suund=="^" or suund=="v" or suund==">":
                break
            else:
                print("Vigane sisend! Proovime uuesti ...")
        except:
            print("Vigane sisend! Proovime uuesti ...")

pykkari_x=int(laius-2-(laius-x))                                                                            #see rida loob maailma v
pykkari_y=int(kõrgus-2-(kõrgus-y)) #need kaks rida lühendavad veidi maailma loovat rida

create_world(laius*"#"+pykkari_y*("\n#"+(laius-2)*" "+"#")+"\n#"+pykkari_x*" "+suund+(laius-3-pykkari_x)*" "+"#"+(kõrgus-3-pykkari_y)*("\n#"+(laius-2)*" "+"#")+"\n"+laius*"#")

def liigu_seinani():
    while not is_wall():
        step()

liigu_seinani()
right()
liigu_seinani()     #pykkar liigub suvalisse maailma nurka
right()

pykkar_a=1
pykkar_b=1

while not is_wall():
    step()
    pykkar_a+=1
right()
while not is_wall():    #pykkar mõõdab maailma ära pykkar_a ja pykkar_b koordinaatides
    step()
    pykkar_b+=1
right()

def liigu_keskele(pykkar):
    bla=0
    if pykkar%2==0:
        while bla<pykkar/2:
            step()
            bla+=1
    else:
        while bla<pykkar_a/2-1:
            step()
            bla+=1

liigu_keskele(pykkar_a)
right()
liigu_keskele(pykkar_b)     #pykkar liigub maailma keskele ja värvib ruudu
paint()

def värvi_ruut():
    right()
    step()
    paint()
    
bla=0
if pykkar_a%2==0:         #siin otsustab programm kas maailma koordinaadid on paarisarvud ning on veel vaja värvida
    bla=1
if pykkar_b%2==0:
    bla=2
if pykkar_a%2==0 and pykkar_b%2==0:
    bla=3
if bla==1:
    värvi_ruut()
if bla==2:
    right()
    värvi_ruut()
if bla==3:
    värvi_ruut()
    värvi_ruut()
    värvi_ruut()