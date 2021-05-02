from tkinter import *
from PIL import Image , ImageTk
root= Tk()
root.title("image sliding app")
#for icon
root.iconbitmap("E:a.ico")
first_image=ImageTk.PhotoImage(Image.open("E:/first.jfif"))
second_image=ImageTk.PhotoImage(Image.open("E:/second.jfif"))
third_image=ImageTk.PhotoImage(Image.open("E:/third.jfif"))
Four_image=ImageTk.PhotoImage(Image.open("E:/fourth.jfif"))
fifth_image=ImageTk.PhotoImage(Image.open("E:/fifth.jfif"))
image_list=[first_image,second_image,third_image,Four_image,fifth_image]
my_label=Label(image=second_image)
my_label.grid(row=1,column=0,columnspan=3)
#function for forward image
def forward(image_number):
    global my_label
    global buttom_forward
    global buttom_back
    global button_exit
    my_label.grid_forget()
    my_label=Label(image=image_list[image_number-1])
    my_label.grid(row=1,column=0,columnspan=3)
    buttom_forward=Button(root,text="forward",command=lambda :forward(image_number+1))
    if image_number==5:
        buttom_forward=Button(root,text="forward",stat=DISABLED)
    buttom_back=Button(root,text="back",command=lambda :back(image_number-1))
    buttom_exit=Button(root,text="exit",command=root.quit())
    buttom_forward.grid(row=5,column=2)
    buttom_back.grid(row=5,column=0)
    buttom_exit.grid(row=5,column=1)


def back(img_number):
    # We willl have global variable to access these
    # variable and change whenever needed
    global label
    global button_forward
    global button_back
    global button_exit
    label.grid_forget()

    # for clearing the image for new image to pop up
    label = Label(image=image_list[img_number - 1])
    label.grid(row=1, column=0, columnspan=3)
    button_forward = Button(root, text="forward",
                            command=lambda: forward(img_number + 1))
    button_back = Button(root, text="Back",
                         command=lambda: back(img_number - 1))
    print(img_number)

    # whenever the first image will be there we will
    # have the back button disabled
    if img_number == 1:
        button_back = Button(root, Text="Back", state=DISABLED)

    label.grid(row=1, column=0, columnspan=3)
    button_back.grid(row=5, column=0)
    button_exit.grid(row=5, column=1)
    button_forward.grid(row=5, column=2)
button_back = Button(root, text="Back", command=back,
                     state=DISABLED)
button_exit = Button(root, text="Exit",
                     command=root.quit)
button_forward = Button(root, text="Forward",
                        command=lambda: forward(1))
button_back.grid(row=5, column=0)
button_exit.grid(row=5, column=1)
button_forward.grid(row=5, column=2)
root.mainloop()