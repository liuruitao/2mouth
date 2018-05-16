class Dog(object):
	def __init__(self,fun):
		print('初始化')
		self.__fun = fun

	def __call__(self):
		print('验证')
		self.__fun()
#现在test就是Dog实例对象，如果要执行test()就会去执行Dog里面的call方法
@Dog  #相当于test = Dog(test)
def test():
	print('hahaha')
test()

class Dog(object):
	def __init__(self,name):
		print('我曹')
		self.__name = name

	def __call__(self):
		print('验证')
		self.__name()
@Dog
def Test():
	print('啦啦')
Test()






















