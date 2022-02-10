
import turtle
import colorsys

t=turtle.Turtle()
s=turtle.Screen()

t.speed(95)
s.bgcolor('black')

n=80
h=0

for i in range(360):
    t.color(colorsys.hsv_to_rgb(h, 0.7, 1))
    h +=1/n

    for j in range(2):
        t.left(90)
        t.forward(i*2)

        for v in range(3):
            t.forward(i*3)
            t.right(120)