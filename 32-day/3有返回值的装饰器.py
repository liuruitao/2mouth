def w1(fun):
	print('正在装饰')
	def inner():
		print('验证')
		ret = fun()
		return ret
	return inner
@w1
def test():
	return '哈哈啊哈哈哈'
ret = test()
print(ret)

