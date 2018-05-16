def w1(fun):
	def inner(*args,**kwargs):
		print('验证')
		ret = fun(*args,**kwargs)
		return ret
	return inner
@w1
def test(a,b):  #有参有返回值
	print('a = %d , b = %d'%(a,b))
	return '哈哈啊哈哈哈'
@w1
def test1():  #无参无返回值
	print('天空飘来五个字')
@w1
def test2(a,b):  #有参无返回值
	print('卧槽我在拔刀')
@w1
def test3():  #无参有返回值
	return '略略略'
test1()
test2(1,2)
print(test3())
print(test(1,2))
 

