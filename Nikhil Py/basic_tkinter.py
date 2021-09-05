from tkinter import Tk, Checkbutton, Button, IntVar

root = Tk()
def get_started():
    if(v1.get()==1):
        print("Selected")
    else:
        print("Not selected")

    if (v2.get() == 1):
        print("Selected")
    else:
        print("Not selected")
    if (v3.get() == 1):
        print("Selected")
    else:
        print("Not selected")
    if (v4.get() == 1):
        print("Selected")
    else:
        print("Not selected")
    if (v5.get() == 1):
        print("Selected")
    else:
        print("Not selected")
    if (v6.get() == 1):
        print("Selected")
    else:
        print("Not selected")

v1=IntVar()
v2=IntVar()
v3=IntVar()
v4=IntVar()
v5=IntVar()
v6=IntVar()

c1=Checkbutton(root, text="first", onvalue=1, offvalue=0, variable=v1)
c2=Checkbutton(root, text="second", onvalue=1, offvalue=0, variable=v2)
c3=Checkbutton(root, text="third", onvalue=1, offvalue=0, variable=v3)
c4=Checkbutton(root, text="fourth", onvalue=1, offvalue=0, variable=v4)
c5=Checkbutton(root, text="fifth", onvalue=1, offvalue=0, variable=v5)
c6=Checkbutton(root, text="sixth", onvalue=1, offvalue=0, variable=v6)
b=Button(root, text="Submit", command=get_started)
c1.grid(row=0, column=0)
c2.grid(row=1, column=0)
c3.grid(row=2, column=0)
c4.grid(row=3, column=0)
c5.grid(row=4, column=0)
c6.grid(row=5, column=0)
b.grid(row=6, column=2)

root.mainloop()
