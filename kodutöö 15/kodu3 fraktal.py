from turtle import *
speed(0)
delay(0)
left(135)
up()
forward(350)
down()
right(135)
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
fraktal(100, 4)
    