
from tkinter import Button,Label,Tk,StringVar,Listbox
from tkinter.filedialog import askdirectory
import os
import pygame
from mutagen.id3 import ID3

root = Tk()

var = StringVar()
listofsongs = []
index = 0
realname = []
choice = 0
songlabel = Label(root,textvariable=var,width=35)
def previous():
    global index
    if (index==0):
        index=len(listofsongs)-1
    else:
        index -=1
        pygame.mixer.music.load(listofsongs[index])
        pygame.mixer.music.play()
        var.set(realname[index])

def nextt():
    global index
    if (index==len(listofsongs)-1):
        index=0
    else:
        index += 1
        pygame.mixer.music.load(listofsongs[index])
        pygame.mixer.music.play()
        var.set(realname[index])
def playorpause():
    global choice
    if (choice==0):
        pygame.mixer.music.pause()
        choice = 1
    else:
        pygame.mixer.music.unpause()
        choice = 0

def selectfolder():
    directory = askdirectory()
    os.chdir(directory)
    for files in os.listdir(directory):
    
            
           if (files.endswith(".mp3")):
              realpath = os.path.realpath(files)
              listofsongs.append(files)
           pygame.mixer.init()
           pygame.mixer.music.load(listofsongs[0])
           pygame.mixer.music.play()
           
        
selectfolder()
label = Label(root,text='')
label.grid()
listbox = Listbox(root)
listbox.config(width = 25, bg='RED',fg='white', font =('CASTELLAR',16,'bold'),bd=5)
listbox.grid(row=0,column=1)
for x in listofsongs:
    listbox.insert(0,x)

bprev = Button(root,text="previous",command=previous,width=10,height=2)
bprev.config(font=("CASTELLER",14,'bold'),bg='grey',fg='white',bd=2)
bnext = Button(root,text="next",command=nextt,width=10,height=2)
bnext.config(font=("CASTELLER",14,'bold'),bg='grey',fg='white',bd=2)
bplay = Button(root,text="play/pause",command=playorpause,width=10,height=2)
bplay.config(font=("CASTELLER",14,'bold'),bg='grey',fg='white',bd=2)




bprev.grid(row=1,column=0)
bplay.grid(row=1,column=1)
bnext.grid(row=1,column=2)

root.title("Simpe Music player")
root.geometry("500x500")
root.mainloop()
