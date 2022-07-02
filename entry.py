from tkinter import *

root = Tk()

e = Entry(root, width=50)
e.pack()
e.insert(0, 'enter your name')

def action():
    myLabel = Label(text=e.get())
    myLabel.pack()

myButton = Button(text='click me!', command=action)
myButton.pack()

root.mainloop()