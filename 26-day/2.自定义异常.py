class ShowError(Exception):
	def __init__(self,len,length):
		self.len = len
		self.length = length

def main():
	try:
		s = input('请输入:')
		if len(s) < 3:
			raise ShowError(len(3),3)
	except ShowError as result:
		print('ShowError:输入的长度是%d,长度至少是%d'%(result.len,result.length))
	else:
		print('没有异常')
main()
