from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox

root=Tk()
root.title("ask yes no")
root.iconbitmap("E:/a.ico")
def popup():
    response=messagebox.askyesno("this is my popup","hello world!!")
    Label(root,text=response).pack()
    if response==1:
        Label(root,text="clicked yes").pack()
    else:
        Label(root,text="clicked no").pack()
Button(root,text="click me",command=popup).pack()
mainloop()