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
 
print('*'*50) 

def w1(name):
	print('正在验证')
	def inner(a,b):
		print('验证中')
		print(a,b)
		ret = name(a,b)
		return ret
	return inner
@w1
def test(a,b):
	print('验证成功')
	return '啦啦啦啦'
ret = test('刘瑞涛','大帅比')
print(ret)



















