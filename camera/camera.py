#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tkinter import *
from PIL import Image, ImageTk
import time
import cv2


root = Tk()
str = StringVar()
label = Label(root, textvariable=str)
label.grid(row=0, column=0)
canvas = Canvas(root, width=800, height=600)
canvas.grid(row=1, column=0)

cap = cv2.VideoCapture(0)


def show():
	global str

	ret, frame = cap.read()
	str.set('frame: ' )
	cov = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
	img = Image.fromarray(cov)
	img = ImageTk.PhotoImage(img)
	
	canvas.create_image(0, 0, anchor=NW, image=img)
	root.update_idletasks()
	root.update()



while (True):
	show()
	cv2.waitKey(200)

# root.mainloop(10000)

cap.release()
cv2.destroyAllWindows()