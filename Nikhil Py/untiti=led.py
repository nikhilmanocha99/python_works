'''from tkinter import Tk, Button
root = Tk()
def sample():
    print('1')
def sample2():
    print('2')

b1 = Button(root, text='To print1', command=sample)
b2 = Button(root, text='To print 2', command=sample2)
b1.pack()
b2.pack()

root.mainloop()'''
'''from tkinter import Tk, messagebox as msc, Button
root = Tk()
def info():
    msc.showinfo('Your name', 'welcome')


def error():
    msc.showerror('Error')

def warn():
    msc.showwarning('warning')
def last():
    quit()

b1 = Button(root, text='Info', command=info)
b2 = Button(root, text='Error', command=error)
b3 = Button(root, text='warn', command=warn)
b4 = Button(root, text='exit', command=last)
b1.grid(row=1, column=1)
b2.grid(row=1, column=2)
b3.grid(row=2, column=1)
b4.grid(row=2, column=2)
root.mainloop()'''
'''
from tkinter import Tk, Entry, Button, Label, messagebox as ms
root = Tk()
def msg():
        name=e.get()
        ms.showinfo('Hello !' ,'have a good day! ' + name)

l = Label(root, text="Enter your name")
e = Entry(root)
b1 = Button(root, text='Submit', command=msg)
l.grid(row=1, column=0)
e.grid(row=1, column=2)
b1.grid(row=2, column=3)
root.mainloop()'''
'''from tkinter import Tk,Entry, StringVar, Label, Button
root = Tk()
def sol():
    data=e.get()
    try:
        result = str(eval(data))
        msg.set(result)
    except:
        msg.set('Invalid Expression')

msg = StringVar()

l = Label(root, text="Expression")
l1 = Label(root, textvariable=msg)
e = Entry(root)
b1= Button(root, text='Solution', command=sol)
l.pack()
l1.pack()
e.pack()
b1.pack()
root.mainloop()
'''
'''from tkinter import Tk, Button, Label, Entry
root = Tk()
def add(a,b):
    pass
def sub(a,b):
    pass
def mul(a,b):
    pass
def dev(a,b):
    pass
def rem(a,b):
    pass
b1=Button(root, text='Add', command=add)
b2=Button(root, text='sub', command=sub)'''
'''
from tkinter import Tk, Listbox
root = Tk()

lis = Listbox(root, bg='sky blue', font=('Algerian', 24))
lis.insert(1, 'Python')
lis.insert(2, 'Java')
lis.grid(row=0, column=1)
root.geometry("300x300")
root.mainloop()'''
'''from tkinter import Tk, Scrollbar, Listbox, Button
root = Tk()
scroll = Scrollbar(root)
def esc():
    quit()

listt = Listbox(root, yscrollcommand=scroll.set)
for i in range(0,100):
    listt.insert(i, " This is line number ")
    

listt.pack(side='left', fill='y')
scroll.config(command=listt.yview())
root.mainloop()'''

'''from tkinter import Tk, Scale, Button, Label
root = Tk()
root.geometry('500x500')
def getval():
    val = sc.get()
    label.config(text='Selected value is: ' + str(val))

label = Label(root)
b = Button(root, text="Get Value", command=getval)
sc = Scale(root, from_=100, to=1000, orient='vertical', length=1000, resolution=50)
sc.set(1000)
sc.pack()
b.pack()
label.pack()
root.mainloop()'''
#Calc
'''from tkinter import Label, Tk, Button, Entry, StringVar
root = Tk()
var = StringVar()
var.set("Expression")
expression = ""
def calc(msg):
    global expression
    expression = expression + msg
    var.set(expression[-20:])

def sol():
    global expression
    try:
        s = eval(expression)
        expression = str(s)
        var.set(expression[-20:])

    except:
        var.set("invalid Expression")
        expression=""

def clean():
    global expression
    expression = ""
    var.set("Enter your expression")

def delete():
    global expression
    expression = expression[:-1]
    var.set(expression[-20:])

b0 = Button(root, text="0", command=lambda :calc("0"))
b1 = Button(root, text="1", command=lambda :calc("1"))
b1.config(font=("algerian, 18"))
b2 = Button(root, text="2", command=lambda :calc("2"))
b2.config(font=("algerian, 18"))
b3 = Button(root, text="3", command=lambda :calc("3"))
b3.config(font=("algerian, 18"))
b4 = Button(root, text="4", command=lambda :calc("4"))
b4.config(font=("algerian, 18"))
b5 = Button(root, text="5", command=lambda :calc("5"))
b5.config(font=("algerian, 18"))
b6 = Button(root, text="6", command=lambda :calc("6"))
b6.config(font=("algerian, 18"))
b7 = Button(root, text="7", command=lambda :calc("7"))
b7.config(font=("algerian, 18"))
b8 = Button(root, text="8", command=lambda :calc("8"))
b8.config(font=("algerian, 18"))
b9 = Button(root, text="9", command=lambda :calc("9"))
b9.config(font=("algerian, 18"))
badd = Button(root, text="+", command=lambda :calc("+"))
badd.config(font=("algerian, 18"))
bsub  = Button(root, text="-", command=lambda :calc("-"))
bsub.config(font=("algerian, 18"))
bmul = Button(root, text="x", command=lambda :calc("*"))
bmul.config(font=("algerian, 18"))
bdiv  = Button(root, text="/", command=lambda :calc("/"))
bdiv.config(font=("algerian, 18"))
bback = Button(root, text="del", command=delete)
bback.config(font=("algerian, 18"))
bclr = Button(root, text="clr", command=clean)
bclr.config(font=("algerian, 18"))
bs = Button(root, text="Ans", command=sol)
bs.config(font=("algerian, 20"))
b0.config(font=("algerian, 18"))
l = Label(root, textvariable=var)
l.config(font=("algerian", "20"))
l.grid(row=1, columnspan=5)
b0.grid(row=6, column=2)
badd.grid(row=3, column=0)
b1.grid(row=3, column=1)
b2.grid(row=3, column=2)
b3.grid(row=3, column=3)
bsub.grid(row=5, column=0)
b4.grid(row=4, column=1)
b5.grid(row=4, column=2)
b6.grid(row=4, column=3)
bmul.grid(row=3, column=4)
b7.grid(row=5, column=1)
b8.grid(row=5, column=2)
b9.grid(row=5, column=3)
bdiv.grid(row=5, column=4)
bback.grid(row=6, column=1)
bclr.grid(row=6, column=3)
bs.grid(row=8, columnspan=5)




root.geometry("300x300")
root.mainloop()'''
