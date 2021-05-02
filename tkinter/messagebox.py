from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
root=Tk()
root.title("message box")
root.iconbitmap("E:a.ico")
def popup():
    #show info message
    messagebox.showinfo("this is my popup","hello world!!")
buttom=Button(root,text="popup",command=popup).pack()
mainloop()