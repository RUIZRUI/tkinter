#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
from PIL import Image, ImageTk
import cv2

# 全局变量，记录日志数
log_num_g = 0
# 全局变量，canvas显示图片
pic_open = None
pic = None

# 界面类
class Camera_GUI():
	def __init__(self, root):
		self.root = root
	
	def initRoot(self):
		'''
			初始化主窗口
		'''
		# 声明全局变量
		global pic_open
		global pic
		
		# 设置窗口名
		self.root.title('标签监视程序 v1.0')
		# 设置窗口大小、窗口的默认弹出位置
		self.root.geometry('1068x681+10+10')
		# Linux 系统窗口最大化
		# self.root.attributes('-zoomed', True)
		# Windows 系统窗口最大化
		self.root.state('zoomed')
		
		# 标签控件
		self.pic_label = Label(self.root, text='摄像头画面')
		# 位置
		self.pic_label.grid(row = 0, column = 0)
		
		# 画布控件
		pic_open = Image.open(r'C:\Users\QIXQI\Desktop\wallpaper\wallpaper\1.jpg')
		# 调整图片大小
		pic_open = pic_open.resize((1200, 800), Image.ANTIALIAS)
		pic = ImageTk.PhotoImage(pic_open)
		self.pic_canvas = Canvas(self.root, width=1250, height=800)
		# 将画布放置到主窗口
		self.pic_canvas.grid(row=2, column=0)
		self.pic_canvas.create_image(50, 0, anchor='nw', image=pic)
		
		
		

# 调用界面类，实例化对象
def camera_start():
	root = Tk()
	Camera_Project = Camera_GUI(root)
	# 初始化主窗口
	Camera_Project.initRoot()
	
	# 主窗口循环，等待消息
	root.mainloop()
	
camera_start()