from turtle import *
from math import sin, cos, sqrt, radians, floor

speed(9999)

def origin():
    setx(0)
    sety(0)

def circleCircle(radius, cirRadius = 5):
    x = 0
    for i in range(361):
        dif_x = pow((cos(radians(x)))-(cos(radians(i))),2)
        dif_y = pow((sin(radians(x)))-(sin(radians(i))),2)
        dif = floor(radius*sqrt(dif_x + dif_y))
        
        if(dif > cirRadius+5):
            x = i;

            penup()
            origin()
            
            setx(sin(radians(i))*radius)
            sety(cos(radians(i))*radius)

            pendown()
            circle(cirRadius)
            penup()


circleCircle(500,100)

origin()
done()

