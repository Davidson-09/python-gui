from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('images implementation')

root.iconbitmap('crab.ico')

my_img = ImageTk.PhotoImage(Image.open('mansnake.jpg'))
my_label = Label(image=my_img)
my_label.pack()

button_quit = Button(root, text='Exit program', command=root.quit)
button_quit.pack()

root.mainloop()