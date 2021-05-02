from tkinter import *
from PIL import ImageTk,Image
root=Tk()
root.title("image insertation")
root.iconbitmap("E:/a.ico")
my_image=ImageTk.PhotoImage(Image.open("E:/cl2.png"))
my_label=Label(image=my_image)
my_label.pack(side=TOP)

my_buttom=Button(root,text="Exit",command=root.quit,width=30)
my_buttom.pack()
root.mainloop()
#adding status bar at the end
status= Label(root,"image 1 of 5")
def in_image():
    status = Label(root,text=str(image_number))

