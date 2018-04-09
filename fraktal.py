from turtle import *
speed(0)
delay(0)
up()
right(225)
forward(500)
right(135)
down()
def kursiiv(number, tase, pikkus):
    if number==1:
        forward(pikkus/tase)
        right(88)
        forward(pikkus/tase)
        right(184)
        forward(pikkus/tase)
        right(88)
        forward(pikkus/tase)
    else:
        kursiiv(number-1, tase, pikkus)
        right(88)
        kursiiv(number-1, tase, pikkus)
        right(184)
        kursiiv(number-1, tase, pikkus)
        right(88)
        kursiiv(number-1, tase, pikkus)
        
def fraktal(pikkus, tase):
    for i in range(4):
        number=tase
        kursiiv(number, tase, pikkus)
        right(90)


fraktal(50, 7) #<--siin teist väärtust muutes saab muuta fraktali taset

exitonclick()

    