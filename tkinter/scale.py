from tkinter import *
root=Tk()
vertical=Scale(root,from_=0,to=200,orient=VERTICAL)
vertical.pack()
horizontal=Scale(root,from_=0,to=200,orient=HORIZONTAL)
horizontal.pack()
def slide():
    my_label=Label(root,text=horizontal.get()).pack()
    root.geometry(str(horizontal.get()) + "x" + str(vertical.get()))
my_btn=Button(root,text="click me",command=slide).pack()
root.mainloop()