from turtle import *
from math import *
a=int(input("mis on a "))
b=int(input("mis on b "))
c=hypot(a,b)
sinalfa=(sin(radians(90))/c)*b
alfa=degrees(asin(sinalfa))
hideturtle()
up()
right(alfa+90)
forward(c*10)
down()
left(alfa+90)
forward(a*20)
left(90)
forward(b*20)
left(alfa+90)
forward(c*20)