from tkinter import Tk, Button, Listbox, StringVar, Label
from tkinter.filedialog import askdirectory
import os
import pygame
root = Tk()
class musicplayer(object):
    def __init__(self, root):
        self.var = StringVar()
        self.var.set("")
        self.li = []
        self.name=[]
        self.index = 0
        songname = Label(root, text="")
        songname.config(font=('Algerian', '18'))
        list = Listbox(root)
        bfol = Button(root, text="Choose folder", command=self.folder)
        bplay = Button(root, text='Play', command=self.play)
        bplay.config(bd=3, font=("Algerian", "16"))
        bps = Button(root, text="Pause", command=self.pause)
        bps.config(bd=3, font=("Algerian", "16"))
        bstop = Button(root, text="Exit", command=self.stop)
        bstop.config(bd=3, font=("Algerian", "16"))
        bnxt = Button(root, text='Next', command=self.next)
        bnxt.config(bd=3, font=("Algerian", "16"))
        bpr = Button(root, text="Previous", command=self.previous)
        bpr.config(bd=3, font=("Algerian", "16"))

        songname.grid(row=0, column=0)
        list.grid(row=1, column=0)
        bplay.grid(row=1, column=3)
        bps.grid(row=2, column=3)
        bnxt.grid(row=3, column=3)
        bpr.grid(row=4, column=3)
        bstop.grid(row=5, column=3)
        bfol.grid(row=6, columnspan=3)



    def play(self):
        pygame.mixer.music.unpause()
    def pause(self):
        pygame.mixer.music.pause()
    def stop(self):
        quit()
    def next(self):
        if (self.index==len(self.li)-1):
            self.index = 0
        else:
            self.index+=1
            pygame.mixer.music.load(self.li[self.index])
            pygame.mixer.music.play()
            self.var.set(self.name[self.index])
    def previous(self):
        if (self.index==0):
            self.index = len(self.li) - 1


        else:
            self.index = self.index-1
            pygame.mixer.music.load(self.li[self.index])
            pygame.mixer.music.play()
            self.var.set(self.name[self.index])
    def folder(self):
        self.direct = askdirectory()
        os.chdir(self.direct)
        for self.file in os.listdir(self.direct):
            if self.file.endswith(".mp3") or self.file.endswith(".mp4"):
                self.rpath = os.path.realpath(self.file)
                self.li.append(self.file)
        pygame.mixer.init()
        pygame.mixer.music.load(self.li[0])
        pygame.mixer.music.play()
        self.var.set(self.name[self.index])



musicplayer(root)
root.mainloop()