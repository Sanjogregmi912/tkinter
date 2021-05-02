'''
from tkinter import *
root = Tk()
def show():
    mylabel= Label(root,text=clicked.get()).pack()
clicked=StringVar()
clicked.set("monday")
drop=OptionMenu(root,clicked,"Monday","tuesday","Wednesday","thursday","friday")
drop.pack()
mybuttom=Button(root,text="show selection",command=show).pack()
mainloop()
'''

from tkinter import *
root=Tk()
def show():
    mylabel=Label(root,text=clicked.get()).pack()
#making option into list
options=[
    "Monday",
    "tuesday",
    "wednesday",
    "thursday",
    "friday"
]
clicked=StringVar()
clicked.set("Monday")
drop=OptionMenu(root,clicked,*options)
drop.pack()
mybutton=Button(root,text="show selection",command=show).pack()
mainloop()
