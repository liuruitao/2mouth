def w1(fun):
	print('正在装饰')
	def inner(a,b):
		print('验证')
		print(a,b)
		ret = fun(a,b)
		return ret
	return inner
@w1
def test(a,b):
	print('hehehehe')
	return '哈哈啊哈哈哈'
ret = test(1,2)
print(ret)
 

