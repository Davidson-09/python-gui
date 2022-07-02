from tkinter import *

root = Tk()
root.title("simple calculator")

global first_number 
first_number = ''
global second_number
second_number=''

e = Entry(root, width=35, border=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def button_click(number):
    current = e.get()
    e.delete(0, END)
    new_input = str(current)+str(number)
    e.insert(0, new_input)

def button_clear():
    e.delete(0, END)
    first_number = ''
    second_number = ''

def button_add():
    first_number = e.get()
    e.delete(0, END)

def button_equal():
    second_number = e.get()
    answer = int() + int(second_number)
    e.delete(0, END)
    e.insert(0, answer)
    first_number=''
    second_number=''



button_1 = Button(text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(text="0", padx=40, pady=20, command=lambda: button_click(0))
button_add = Button(text="+", padx=39, pady=20, command=button_add)
button_equal = Button(text="=", padx=91, pady=20, command=button_equal)
button_clear = Button(text="clear", padx=79, pady=20, command=button_clear)

# put the buttons on the screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_0.grid(row=4, column=0)
button_add.grid(row=4, column=1)
button_equal.grid(row=5, column=0, columnspan=2)
button_clear.grid(row=5, column=1, columnspan=2)

root.mainloop()