from tkinter import *
root=Tk()

def show():
    my_label=Label(root,text=var.get()).pack()
var = StringVar()
#anything can be written in or off string input
checkbuttom=Checkbutton(root,text="check this box",variable=var,onvalue="on",offvalue="off")
checkbuttom.deselect()
checkbuttom.pack()
mybuttom=Button(root,text="show selection",command=show).pack()
mainloop()