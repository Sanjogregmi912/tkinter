from tkinter import *
root=Tk()
def clickme():
    mylabel=Label(root,text="button is clicked")
    mylabel.pack()
mybutton=Button(root,text="click me",command=clickme)

mybutton.pack()
root.mainloop()