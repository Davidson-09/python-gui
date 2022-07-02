from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text="clicked button!")
    myLabel.pack()

# define the thing
myButton = Button(root, text='click me', padx=50, pady=50, command=myClick, fg="blue", bg="white")

myButton.pack()

root.mainloop()