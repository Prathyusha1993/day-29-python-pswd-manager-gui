from tkinter import *

window = Tk()

r = Label(bg='red', width=20, height=5)
r.grid(column=0, row=0)

l = Label(bg='green', width=20, height=5)
l.grid(row=1, column=1)

b = Label(bg='blue', width=40, height=5)
b.grid(row=2, column=0, columnspan=2)

window.mainloop()