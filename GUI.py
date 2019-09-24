import tkinter

from tkinter import Tk
from tkinter import ttk
from tkinter import *

# root=Tk()
# root.title("First GUI using Python")
# ttk.Button(root, text="Hello").grid()
# root.mainloop()

# frame = Frame(root)
# labelText = StringVar()
# label = Label(frame,textvariable = labelText)
# button=Button(frame, text = "button")
# labelText.set("Hey!")
# label.pack()
# button.pack()
# frame.pack()
# root.mainloop()

# frame = Frame(root)
# Label(frame, text="Hey").pack()
# Button(frame,text="B1").pack(side=LEFT, fill = Y)
# Button(frame,text="B2").pack(side=RIGHT, fill = X)
# Button(frame,text="B3").pack(side=TOP, fill = Y)
# Button(frame,text="B4").pack(side=LEFT, fill = Y)
#
# frame.pack()
# root.mainloop()

# Label(root, text="Name").grid(row=0,column=0, sticky=N)
# Entry(root, width=50).grid(row=0, column=1)
# Button(root, text="Submit").grid(row=0, column=5)
#
# Label(root, text="Gender").grid(row=1, column=0, sticky=N)
# Radiobutton(root, text="F", value=1).grid(row=1, column=1, sticky=N)
# Radiobutton(root, text="M", value=2).grid(row=1, column=2, sticky=N)
#
# Label(root, text="Courses").grid(row=2, column=0, sticky=N)
# Checkbutton(root, text="Python").grid(row=3,column=1, sticky=N)
# Checkbutton(root, text="Djano").grid(row=4,column=1, sticky=N)
# Checkbutton(root, text="Flask").grid(row=5,column=1, sticky=N)
# root.mainloop()

def square(event):
    a=int(num1.get())
    b=a*a
    result.delete(0,"end")
    result.insert(0,b)

root=Tk()

Label(root, text="Find the square").pack()
num1 = Entry(root)
num1.pack(side=LEFT)

btn = Button(root, text="Squares to")
btn.bind("<Button-1>", square)
btn.pack(side=LEFT)

result = Entry(root)
result.pack(side=LEFT)

root.mainloop()