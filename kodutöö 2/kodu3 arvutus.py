pikkus=int(input("tordi pikkus küpsistes "))
laius =int(input("tordi laius küpsistes "))
kõrgus=int(input("tordi kõrgus küpsistes "))
pakk=int(input("pakis on küpsiseid "))
arv=(pikkus*laius*kõrgus%pakk)
vastus=(pikkus*laius*kõrgus//pakk)
if arv>=0.5*pakk:
    print(vastus+1)
elif arv<0.5*pakk:
    print(vastus)