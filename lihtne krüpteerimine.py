def krüpteeri_sõne(tekst):
    print(tekst)
    krüpt=[]
    järjend=""
    järjend=list(tekst)
    for i in järjend:
        x=ord(i)
        z=str(x*519//7)
        krüpt+=[z]
    return "".join(krüpt)
print(krüpteeri_sõne("Mina olen Kaspar."))