#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
import tkinter.messagebox
from PIL import Image, ImageTk
import cv2
import os
import threading
import util

# 全局变量，记录日志数
log_num_g = 0
# 全局变量，canvas显示图片
# pic_open = None
# pic = None
# 全局变量，图像刷新时间间隔
interval_time = 200
# 全局变量，图像像素精度
CAP_PIC_WIDTH = 1280
CAP_PIC_HEIGHT = 720

# 界面类
class Camera_GUI():
	def __init__(self, root, cap):
		'''
			root 主窗口元素
			cap 本机摄像头对象
		'''
		self.root = root
		self.cap = cap
		
		# capIdx，存储图片下标
		self.capIdx = 0
		# frameBak，保存上次画面
		self.frameBak = None
		# cavWidth，画布宽度
		cavWidth = None
		# cavHeight，画布高度
		cavHeight = None
		
		# 初始化参数
		self.initParam()
	
	
	def initParam(self):
		''' 
			初始化参数 frameBak，cavWidth，cavHeight
		''' 
		# 刚打开相机时，曝光不稳定，清理10张
		for i in range(10):
			ret, self.frameBak = self.cap.read()
		self.cavWidth = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
		self.cavHeight = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
		print('图片宽度：{}，图片高度：{}'.format(self.cavWidth, self.cavHeight))
		
		
		
	
	def initRoot(self):
		'''
			初始化主窗口
		'''
		# 声明全局变量
		# global pic_open
		# global pic
		global interval_time
		
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
		# pic_open = Image.open(r'C:\Users\QIXQI\Desktop\wallpaper\1.jpg')
		# 调整图片大小
		# pic_open = pic_open.resize((1200, 800), Image.ANTIALIAS)
		# pic = ImageTk.PhotoImage(pic_open)
		# self.pic_canvas = Canvas(self.root, width=1250, height=800)
		self.pic_canvas = Canvas(self.root, width=self.cavWidth+20, height=self.cavHeight)
		# 将画布放置到主窗口
		self.pic_canvas.grid(row=2, column=0)
		
		# 滚动条控件
		# self.bottom_scrollbar = Scrollbar(self.root, cursor='spider')
		# self.bottom_scrollbar.grid(side=5, fill=X)
		
		
		# 循环更新图像
		# self.pic_canvas.create_image(50, 0, anchor='nw', image=pic)
		while (True):
			self.updatePic()
			if cv2.waitKey(interval_time) & 0xff == ord('q'):
				# 按 'q' 键无效，因为不是 cv2.imshow显示页面
				break
		
	
	def getPic(self):
		# 读取摄像头图像
		ret, frame = self.cap.read()
		cov = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
		pic_open = Image.fromarray(cov)
		# 调整图像大小
		# pic_open = pic_open.resize((1200, 800), Image.ANTIALIAS)
		pic = ImageTk.PhotoImage(pic_open)
		return pic, frame
	
	def updatePic(self):
		'''
			循环更新图像
		'''
		pic, frame = self.getPic()
		self.pic_canvas.create_image(20, 0, anchor='nw', image=pic)
		# 更新主窗口元素
		self.root.update_idletasks()
		self.root.update()
		# 默认停顿200ms
		# cv2.waitKey(interval_time)
		
		# 判断图像是否变化
		self.isPicChanged(frame)
		
	
	def destroyPic(self):
		# 函数是引用传递，只需释放一次
		self.cap.release()
		cv2.destroyAllWindows()
		
	
	def isPicChanged(self, frame, dividePar=4, pointerDelta=50, judgeTh=64):
		''' 
			frame: 当前图像
			dividePar: 对比隔点，减少计算量（4）
			pointerDelta: 像素点差异大于该值认为是差异点（50）
			judgeTh: 判断画面是否变化的阈值（64）
		''' 
		# 记录前后两张图像，变化像素点的个数
		# absCnt = 0
		# # 计算变化像素点个数
		# for wIdx in range(int(self.cavWidth/dividePar)):
		# 	for hIdx in range(int(self.cavHeight/dividePar)):
		# 		if abs(int(self.frameBak[hIdx*dividePar][wIdx*dividePar][2]) - int(frame[hIdx*dividePar][wIdx*dividePar][2])) > pointerDelta:
		# 			# 变化像素点加一
		# 			absCnt += 1 	
		
		# # 判断图像变化是否大于阈值
		# if absCnt > (self.cavHeight * self.cavWidth) / (dividePar * dividePar) / (judgeTh * judgeTh):
		# 	# 大于阈值，保存图像
		# 	self.capIdx += 1 
		# 	cv2.imwrite('cap/cap_{}.jpg'.format(self.capIdx), frame)
		# 	print('get a pic: cap_{}.jpg'.format(self.capIdx))
		
		# # 更新 frameBak
		print(self.calculate(frame))
		self.frameBak = frame

		
	
	def calculate(self, frame):
	    # 灰度直方图算法
	    # 计算单通道的直方图的相似值
	    hist1 = cv2.calcHist([frame], [0], None, [256], [0.0, 255.0])
	    hist2 = cv2.calcHist([self.frameBak], [0], None, [256], [0.0, 255.0])
	    # 计算直方图的重合度
	    degree = 0
	    for i in range(len(hist1)):
	        if hist1[i] != hist2[i]:
	            degree = degree + \
	                (1 - abs(hist1[i] - hist2[i]) / max(hist1[i], hist2[i]))
	        else:
	            degree = degree + 1
	    degree = degree / len(hist1)
	    return degree
	
	


class Camera_Engine():
	''' 
		引擎类，用于更改 Camera_GUI对象的属性
	''' 
	def __init__(self, frame):
		global interval_time
		
		self.frame = frame
		self.interval = StringVar()
		self.interval.set(str(interval_time))
	
	def initFrame(self):
		# 间隔时间
		self.interval_time_label = Label(self.frame, text='间隔时间（50-500ms）：')
		self.interval_time_label.grid(row=0, column=0)
		self.interval_spinbox = Spinbox(self.frame, from_=50, to=500, textvariable=self.interval)
		self.interval_spinbox.grid(row=2, column=0)
	
		# 调整按钮
		self.edit_btn = Button(self.frame, text='调整', bg='green', command=self.editInterval)
		self.edit_btn.grid(row=4, column=0)
		
	def editInterval(self):
		# 全局变量，间隔时间
		global interval_time
		
		interval1 = self.interval_spinbox.get()
		interval1 = util.to_Inumber(interval1)
		if interval1 is not None:
			# 字符串转整数成功
			if interval1 < 50:
				# 小于50ms，置为50ms
				interval_time = 50
			elif interval1 > 500:	
				# 大于500ms，置为500ms
				interval_time = 500
			else:
				# 转为整型
				interval_time = interval1
			
			self.interval.set(str(interval_time))
		else:
			# 输入异常，不是数字
			# 消息弹窗
			tkinter.messagebox.showerror('error', '输入不是数字')
			self.interval.set('')
		

# 调用界面类，实例化对象
def camera_start():
	global CAP_PIC_WIDTH
	global CAP_PIC_HEIGHT
	
	# 创建文件夹
	if not os.path.exists('cap'):
		os.makedirs('cap')

	root = Tk()
	cap = cv2.VideoCapture(0)
	
	# 设置图像像素
	cap.set(cv2.CAP_PROP_FRAME_WIDTH, CAP_PIC_WIDTH)
	cap.set(cv2.CAP_PROP_FRAME_HEIGHT, CAP_PIC_HEIGHT)
	
	Camera_Project = Camera_GUI(root, cap)
	
	# 初始化摄像机引擎
	frame = Frame(root, width=180, height=500, bd=1)
	frame.grid(row=2, column=210, sticky=N)
	cEngine = Camera_Engine(frame)
	# 开启线程
	# t = threading.Thread(target = cEngine.initFrame)
	# t.setDaemon(True)	# 守护进程
	cEngine.initFrame()
	# t.start()

	# 初始化摄像机画面
	# 开启线程
	# t = threading.Thread(target = Camera_Project.initRoot)
	# t.setDaemon(True)
	# t.start()
	Camera_Project.initRoot()
	
	# 主窗口循环，等待消息
	root.mainloop()
	
	# 释放cap
	Camera_Project.destroyPic()









if __name__ == '__main__':
	# 异常处理	
	try: 
		camera_start()
	except RuntimeError:
		# 程序运行过程中，按下关闭按钮'x'
		print('RuntimeError')
		os._exit(0)