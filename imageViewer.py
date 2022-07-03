from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('image viewer')
root.iconbitmap('crab.ico')

my_img1 = ImageTk.PhotoImage(Image.open('view.jpg'))
my_img2 = ImageTk.PhotoImage(Image.open('bird.jpg'))
my_img3 = ImageTk.PhotoImage(Image.open('pepper.jpg'))
my_img4 = ImageTk.PhotoImage(Image.open('mansnake.jpg'))

image_list = [my_img1, my_img2, my_img3, my_img4]

my_label = Label(image=my_img1)
my_label.grid(row=2, column=0, columnspan=3)

button_back = Button(root, text="<<")
button_exit = Button(root, text="EXIT PROGRAM")
button_forward = Button(root, text=">>")

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)

root.mainloop()