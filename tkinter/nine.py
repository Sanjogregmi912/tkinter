from tkinter import *
root=Tk()
e1=Entry(root,width=50,fg="blue",bg="red",borderwidth=5)
e1.pack(side=TOP)
def myclick():
    mylabel=Label(root,text="hello"+ " "+ e1.get())
    mylabel.pack(side=BOTTOM)
mybutton=Button(root,text="submit",command=myclick,bg="black",fg="blue")
mybutton.pack()
root.mainloop()