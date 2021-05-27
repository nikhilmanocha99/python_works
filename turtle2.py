import turtle
import random
from turtle import *
from turtle import Turtle

nik = turtle.Turtle()
nik.speed(-1)
nik.width(5)
nik.shape('turtle')

colors = ['red', 'blue', 'green', 'yellow', 'orange', 'black']

def up():
    nik.setheading(90)
    nik.forward(100)

def  left():
    nik.setheading(180)
    nik.forward(100)

def down():
    nik.setheading(270)
    nik.forward(100)

def right():
    nik.setheading(0)
    nik.forward(100)

def leftclick(x,y):
    nik.color(random.choice(colors))

def rightclick(x,y):
    nik.stamp()

turtle.listen()

turtle.onscreenclick(leftclick, 1)
turtle.onscreenclick(rightclick, 3)
turtle.onkey(up,'Up')
turtle.onkey(left,'Left')
turtle.onkey(down,'Down')
turtle.onkey(right,'Right')


turtle.mainloop()