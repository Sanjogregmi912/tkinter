from tkinter import *
root=Tk()
root.title("radio")
modes=[
    ("pepperoni","pepperoni"),
    ("cheese","cheese"),
    ("mushroom","mushroom"),
    ("onion","onion")
]
pizza=StringVar()
pizza.set("pepperoni")
f C
for text,mode in modes:
    Radiobutton(root,text=text,variable=pizza,value=mode).pack(anchor=W)
def clicked(value):
    mylabel=Label(root,text=value)
    mylabel.pack()
my_button=Button(root,text="click",command=lambda :clicked(pizza.get())).pack()
root.mainloop()

