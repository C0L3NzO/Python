from turtle import *
from random import randint
nurgad=int(input("Mis on nurkade arv? "))
küljed=int(input("Mis on külgede pikkus? "))
nurk=180-((nurgad-2)*180)/nurgad
def kujund():
    joonistatud=0
    while joonistatud<nurgad:
        forward(küljed)
        right(nurk)
        joonistatud+= 1
def suva():
    up()
    forward(randint(50,100))
    left(randint(1,360))
    down()
kordi=0
while kordi<30:
    kujund()
    suva()
    kordi+=1
exitonclick()