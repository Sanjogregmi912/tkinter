from tkinter import *
root=Tk()
mylabel1=Label(root,text="hi")
mylabel2=Label(root,text="you are welcome")
mylabel3=Label(root,text="thank you")
mylabel1.grid(row=0,column=1)
mylabel2.grid(row=1,column=2)
mylabel3.grid(row=2,column=3)
root.mainloop()