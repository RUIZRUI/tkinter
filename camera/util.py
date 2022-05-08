#!/usr/bin/env python
# -*- coding: utf-8 -*-

def is_number(str):
	try: 
		float(str)
		# 字符串 str是浮点数
		return True
	except ValueError:	# 无效参数
		pass
	
	try: 
		# 处理Ascii码
		import unicodedata
		# 把一个表示数字的字符串转换为浮点数返回
		unicodedata.numeric(str)
		return True
	except (TypeError, ValueError):
		pass
	
	return False


def to_Inumber(str):
	''' 
		字符串转为整数
	''' 
	try:
		# 整型字符串
		return int(str)
	except ValueError:
		pass
	
	try: 
		return int(float(str))
		# 字符串 str是浮点数
	except ValueError:	# 无效参数
		pass
	
	try: 
		# 处理Ascii码
		import unicodedata
		# 把一个表示数字的字符串转换为浮点数返回
		return int(unicodedata.numeric(str))
	except (TypeError, ValueError):
		pass
	
	return None