from tkinter import *
root=Tk()
#button without any functiom
mybutton=Button(root,text="click me")
mybutton.pack(side=TOP)
#button with diabled buttom

mybutton1=Button(root,text="click",state=DISABLED)
mybutton1.pack(side=LEFT)
mybutton2=Button(root,text="click",padx=50)
mybutton2.pack(side=RIGHT)
mybutton3=Button(root,text="click if yo want",padx=50,pady=50)
mybutton3.pack(side=BOTTOM)
root.mainloop()