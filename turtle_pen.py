import turtle
from turtle import Turtle, Screen

screen = Screen()
n = Turtle("turtle")
n.speed(-1)

def dragging(x,y):
    n.ondrag(None)
    n.setheading(n.towards(x,y))
    n.goto(x,y)
    n.ondrag(dragging)

def rightclick(x,y):
    n.clear()


def main():
    
    turtle.listen()
    n.ondrag(dragging)

    turtle.onscreenclick(rightclick, 3)
    screen.mainloop()

main()
