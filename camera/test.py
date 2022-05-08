import cv2
import numpy as np 

def isPicChanged(self, frame, dividePar=4, pointerDelta=50, judgeTh=64):
	''' 
		frame: 当前图像
		dividePar: 对比隔点，减少计算量（4）
		pointerDelta: 像素点差异大于该值认为是差异点（50）
		judgeTh: 判断画面是否变化的阈值（64）
	''' 
	# 记录前后两张图像，变化像素点的个数
	absCnt = 0
	# 计算变化像素点个数
	for wIdx in range(int(self.cavWidth/dividePar)):
		for hIdx in range(int(self.cavHeight/dividePar)):
			if abs(int(self.frameBak[hIdx*dividePar][wIdx*dividePar][2]) - int(frame[hIdx*dividePar][wIdx*dividePar][2])) > pointerDelta:
				# 变化像素点加一
				absCnt += 1 	
	
	# 判断图像变化是否大于阈值
	if absCnt > (self.cavHeight * self.cavWidth) / (dividePar * dividePar) / (judgeTh * judgeTh):
		# 大于阈值，保存图像
		self.capIdx += 1 
		cv2.imwrite('cap/cap_{}.jpg'.format(self.capIdx), frame)
		print('get a pic: cap_{}.jpg'.format(self.capIdx))
	
	# 更新 frameBak
	self.frameBak = frame



if __name__ == '__main__':
	img_path = r'C:\Users\QIXQI\Desktop\wallpaper\WIN_20210423_14_20_47_Pro.jpg'
	img = cv2.imread(img_path)
	img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
	img_blur = cv2.medianBlur(img_gray, 7)
	print(img)
	cv2.imshow('img_gray', img_gray)
	cv2.imshow('img_blur', img_blur)
	print(img_gray)
	print(img_blur)
	cv2.waitKey()
	
	