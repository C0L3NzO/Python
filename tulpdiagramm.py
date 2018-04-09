from turtle import *
laius=20
left(90)
def tulp(laius, kõrgus, värv):
    color(värv)
    forward(kõrgus)
    right(90)
    forward(laius)
    right(90)
    forward(kõrgus)
    left(180)
f=open("tulpdiagramm.txt")
while f.readline != "":
    number=int(f.readline().strip())
    if number>50:
        värv=("#0000ff")
    if number<=50:
        värv=("#ff0000")
    tulp(laius, number, värv)
f.close()
exitonclick()