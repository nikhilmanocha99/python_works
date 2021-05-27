import turtle
import math
import random

win_length = 500
win_height = 500
turtles = 6
turtle.screensize(win_length, win_height)
nik = turtle.Turtle()

colors = ['red', 'blue', 'green', 'yellow', 'orange', 'black']
class racer(object):
    def __init__(self, color, pos):
        self.color = color
        self.pos = pos
        self.nik = nik
        self.nik.shape('turtle')
        self.nik.color(random.choice(colors))
        self.nik.penup()
        self.nik.setpos(pos)
        self.nik.setheading(90)

    def move(self):
        r = random.randrange(1,20)
        self.pos = (self.pos[0], self.pos[1] + r)
        self.nik.pendown()
        self.nik.forward(r)

    def reset(self):
        self.nik.penup()
        self.nik.pos(self.pos)

    def setfile(self):
        f = open('scores.txt', 'w')
        for color in colors:
            f.write(color + '0 \n')
        f.close()

    def startgame(self):
        tlist = []
        turtle.clearscreen()
        turtle.hideturtle()
        start = -(win_length/2) + 20
        for t in range(turtles):
            newposx = start + t*(win_length)//turtles
            tlist.append(racer(colors[t], (newposx, -230)))
            tlist[t].nik.showturtle()

        run = True
        while run:
            for t in tlist:
                t.move()

            maxcolor = []
            maxdis  = 0
            for t in tlist:
                if t.pos[1]>230 and t.pos[1]>maxdis:
                    maxdis = t.pos[1]
                    maxcolor = []
                    maxcolor.append(t.color)
                elif t.pos[1]>230 and t.pos[1]==maxdis:
                    maxdis = t.pos[1]
                    maxcolor.append(t.color)

            if len(maxcolor)>0:
                run = False
                print("the winner is: ")

            for win in maxcolor:
                print(win)
        oldscore = []
        file = open('scores.txt', 'r')
        for line in file:
            l = line.split()
            color = l[0]
            score = l[1]
            oldscore.append([color, score])
        file.close()

        file = open('scores.txt', 'w')
        for entry in oldscore:
            for winner in maxcolor:
                if entry[0]==winner:
                    entry[1] = int(entry[1]) + 1
            file.write(str(entry[0]) + '' + str(entry[1]) + '\n')

        file.close()

start = input('would you like to play..!')
racer()
startgame()

while True:
    print('----------------------------')
    start = input('would you like to play again')
    startgame()