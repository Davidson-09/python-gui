import tkinter as tk

def show_frame(frame):
    frame.tkraise()

window = tk.Tk()
window.state('zoomed')

window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)

frame1 = tk.Frame(window)
frame2 = tk.Frame(window)
frame3 = tk.Frame(window)

for frame in (frame1, frame2, frame3):
    frame.grid(row=0, column=0, sticky='nsew')

# frame 1 code
frame1_title = tk.Label(frame1, text='this is frame 1', bg='red')
frame1_title.pack(fill='x')

frame1_btn = tk.Button(frame1, text='NEXT PAGE', command= lambda: show_frame(frame2))
frame1_btn.pack()

# frame 2 code
frame2_title = tk.Label(frame2, text='this is frame 2', bg='yellow')
frame2_title.pack(fill='x')

frame2_btn = tk.Button(frame2, text='NEXT PAGE', command= lambda: show_frame(frame3))
frame2_btn.pack()

# frame 3 code
frame3_title = tk.Label(frame3, text='this is frame 3', bg='green')
frame3_title.pack(fill='x')

frame3_btn = tk.Button(frame3, text='NEXT PAGE', command= lambda: show_frame(frame1))
frame3_btn.pack()

show_frame(frame1)

window.mainloop()