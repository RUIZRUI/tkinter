#!/usr/bin/python
import tkinter

root = tkinter.Tk()

li = ['C', 'python', 'php', 'html', 'sql']
movie = ['css', 'jquery', 'bootstrap']
list1 = tkinter.Listbox(root)
list2 = tkinter.Listbox(root)

for item in li:
	list1.insert(0, item)

for item in movie:
	list2.insert(0, item)

list1.pack()
list2.pack()
root.mainloop()