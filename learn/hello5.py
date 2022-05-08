from tkinter import *


root = Tk()

# root.geometry("200x200")
# root.title("Question 2")
# root.configure(background="green")

parent = Frame(root)
Label(parent, text = "RED", fg="red", bg="black").pack(fill="x")
Label(parent, text = "WHITE", fg="white", bg="black").pack(fill="x")
Label(parent, text = "BLUE", fg="blue", bg="black").pack(fill="x")
parent.pack(expand=1)  # same as expand=True

root.mainloop()