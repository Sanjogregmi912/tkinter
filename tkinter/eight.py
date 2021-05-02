from tkinter import *
root=Tk()
def clickme():
    mylabel=Label(root,text="button is clicked")
    mylabel.pack(side=TOP)

mybutton=Button(root,text="click me",command=clickme,fg="black",bg="blue")
mybutton.pack(side=BOTTOM)
root.mainloop()