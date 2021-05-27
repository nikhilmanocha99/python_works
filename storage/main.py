from tkinter import *
from tkinter import messagebox
import tkinter.messagebox

objects = []
root = Tk()
root.withdraw()
root.title("Email space")


class PopupWindow(object):
  
    loop = False
    attempts = 0
  
    def __init__(self, master):
        top = self.top = Toplevel(master)
        top.title('Input password')
        top.geometry('{}x{}'.format(250, 100))
        top.resizable(width=False, height=False)
        self.l = Label(top, text="Password", font=('Arial', 18), justify=CENTER)
        self.l.pack()
        self.e = Entry(top, show='*', width=30)
        self.e.pack(pady=7)
        self.b = Button(top, text='Submit', command=self.cleanup, font=('Arial', 18))
        self.b.pack()

    def cleanup(self):
        self.value = self.e.get()
        access = '123'

        if self.value == access:
            self.loop = True
            self.top.destroy()
            root.deiconify()

        else:
            self.attempts += 1
            if self.attempts == 5 :
                root.quit()
            self.e.delete(0, 'end')
            messagebox.showerror('Incorrecr Password', 'Incorrect Password attempts remaining: ' + str(5-self.attempts))


class entityadd:
    def __init__(self, master, n, p, e):
        self.password = p
        self.name = n
        self.email = e
        self.root = master

    def write(self):
        f = open('emails.txt', "a")
        n = self.name
        e = self.email
        p = self.password

        encryptedN = ""
        encryptedE = ""
        encryptedP = ""
        for letter in n:
            if letter == ' ':
                encryptedN += ' '
            else:
                encryptedN += chr(ord(letter) + 5)

        for letter in e:
            if letter == ' ':
                encryptedE += ' '
            else:
                encryptedE += chr(ord(letter) + 7)

        for letter in p:
            if letter == ' ':
                encryptedP += ' '
            else:
                encryptedP += chr(ord(letter) + 9)

        f.write(encryptedN + ',' + encryptedE + ',' + encryptedP + ',\n')
        f.close()

class entitydisplay:
    def __init__(self, master, n, e, p, i):
        self.password = p
        self.name = n
        self.email = e

        self.root = master
        self.i = i

        dencryptedN = ""
        dencryptedE = ""
        dencryptedP = ""
        for letter in self.name:
            if letter == ' ':
                dencryptedN += ' '
            else:
                dencryptedN += chr(ord(letter) - 5)
        for letter in self.email:
            if letter == ' ':
                dencryptedE += ' '
            else:
                dencryptedE += chr(ord(letter) - 7)
        for letter in self.password:
            if letter == ' ':
                dencryptedP += ' '
            else:
                dencryptedP += chr(ord(letter) - 9)

        self.label_name = Label(self.root, text=dencryptedP, font=('Arial', 14))
        self.label_email = Label(self.root, text=dencryptedE, font=('Arial', 14))
        self.label_password = Label(self.root, text=dencryptedN, font=('Arial', 14))
        self.deletebt = Button(self.root, text='X', fg='red', command=self.delete, font=(22))

    def display(self):
        self.label_name.grid(row=6 + self.i, sticky=W)
        self.label_email.grid(row=6 + self.i, column=1)
        self.label_password.grid(row=6 + self.i, column=2, sticky=E)
        self.deletebt.grid(row=6 + self.i, column=3, sticky=E)

    def delete(self):
        answer = tkinter.messagebox.askquestion('Are you sure you want to delete this entry? ')
        if answer == 'yes':
            for i in objects:
                i.destroy()
            f = open("emails.txt", 'r')
            lines = f.readline()
            f.close()

            f = open('emails.txt', 'w')
            count = 0

            for line in lines:
                if count != self.i:
                    f.write(line)
                    count += 1
            f.close()
            readfile()

    def destroy(self):
        self.label_name.destroy()
        self.label_email.destroy()
        self.label_password.destroy()
        self.deletebt.destroy()

#functions we are gonna use outside the class
def onsubmit():
    m = email.get()
    p = password.get()
    n = name.get()
    e = entityadd(root, p, n, m)
    e.write()
    name.delete(0, 'end')
    email.delete(0, 'end')
    password.delete(0, 'end')
    messagebox.showinfo('Added entity', 'Successfully added, \n'+ "Name : " + n + "\nEmail : " + m + "\nPassword : " + p)
    readfile()

def clearfile():
    f = open("emails.txt", 'w')
    f.close()

def readfile():
    f = open('emails.txt', 'r')
    count = 0

    for line in f:
        lines = line.split(',')
        e = entitydisplay(root, lines[0], lines[1], lines[2], count)
        objects.append(e)
        e.display()
        count+=1
    f.close()

m = PopupWindow(root)

entity_label = Label(root, text='Add entity', font=('Arial', 20))
entity_name = Label(root, text='Enter Name', font=('Arial', 17))
entity_email = Label(root, text='Enter email', font=('Arial', 17))
entity_password = Label(root, text='Enter password', font=('Arial', 17))
name = Entry(root, font=('Arial', 11))
email = Entry(root, font=('Arial', 11))
password = Entry(root, show='*', font=('Arial', 11))
submit = Button(root, text='Add entry', command=onsubmit, font=('Courier', 20))

entity_label.grid(columnspan=3, row=0)
entity_name.grid(row=1, sticky=E, padx=3)
entity_email.grid(row=2, sticky=E, padx=3)
entity_password.grid(row=3, sticky=E, padx=3)

name.grid(columnspan=3, row=1, column=1, padx=2, pady=2, sticky=W)
email.grid(columnspan=3, row=2, column=1, padx=2, pady=2, sticky=W)
password.grid(columnspan=3, row=3, column=1, padx=2, pady=2, sticky=W)

submit.grid(columnspan=3, pady=4)

name_label = Label(root, text='Name', font=('Arial', 18))
email_label = Label(root, text='Email', font=('Arial', 18))
password_label = Label(root, text='Password', font=('Arial', 18))

name_label.grid(row=5, column=0)
email_label.grid(row=5, column=1)
password_label.grid(row=5, column=2)

readfile()

root.mainloop()
