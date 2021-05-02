from tkinter import *
root =Tk()
#creating a buttom widget
greenbutton = Button(root,text="left",fg="green")
#saving it onto the screen
greenbutton.pack(side= LEFT)
blackbutton=Button(root,text="right",fg="black")
blackbutton.pack(side = RIGHT)
bluebutton= Button(root,text="top",fg="blue")
bluebutton.pack(side = TOP)
redbutton=Button(root,text="bottom",fg="red")
redbutton.pack(side=BOTTOM)
root.mainloop()


