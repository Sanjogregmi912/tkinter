from tkinter import *
from PIL import ImageTk,Image
root=Tk()
root.title("image viewer")

def forward(image_number):
    #global variable to access and change whenever we need
    global my_label
    global buttom_forward
    global buttom_back
    global buttom_quit
    my_label.grid_forget()
    #this is for clearing the screen so that our image can pop up
    my_label=Label(image=list_image[image_number-1])
    #as the list start from zero
    my_label.grid(row=1,column=0,columnspan=3)
    buttom_forward=Button(root,text=">>",command=lambda :forward(image_number+1))
    #image_number+1 is done so that our next image can pop up
    if image_number==5:
        buttom_forward=Button(root,text=">>",stat=DISABLED)
    buttom_back=Button(root,text="<<",command=lambda :back(image_number-1))
    buttom_forward.grid(row=5,column=2)
    buttom_quit.grid(row=5,column=1)
    buttom_back.grid(row=5,column=0)
def back(image_number):
    global my_label
    global buttom_forward
    global buttom_back
    global buttom_quit
    my_label.grid_forget()
    my_label=Label(image=list_image[image_number-1])
    my_label.grid(row=1,column=0,columnspan=3)
    buttom_forward=Button(root,text=">>",command=lambda :forward((image_number+1)))
    buttom_back=Button(root,text="<<",command=lambda : back(image_number-1))
    print(image_number)
    if image_number==1:
        buttom_back=Button(root,text="<<",stat=DISABLED)
    my_label.grid(row=1,column=0,columnspan=3)
    buttom_back.grid(row=5,column=0)
    buttom_quit.grid(row=5,column=1)
    buttom_forward.grid(row=5,column=2)
image1=ImageTk.PhotoImage(Image.open("E:/first.jfif"))
image2=ImageTk.PhotoImage(Image.open("E:/second.jfif"))
image3=ImageTk.PhotoImage(Image.open("E:/third.jfif"))
image4=ImageTk.PhotoImage(Image.open("E:/fourth.jfif"))
image5=ImageTk.PhotoImage(Image.open("E:/fifth.jfif"))
list_image=[image1,image2,image3,image4,image5]
my_label=Label(image=image1)
my_label.grid(row=1,column=0,columnspan=3)
buttom_back=Button(root,text="<<",command=back,stat=DISABLED)
buttom_forward=Button(root,text=">>",command=lambda :forward(1))
buttom_quit=Button(root,text="quit",command=root.quit)
buttom_back.grid(row=5,column=0)
buttom_quit.grid(row=5,column=1)
buttom_forward.grid(row=5,column=2)
root.mainloop()