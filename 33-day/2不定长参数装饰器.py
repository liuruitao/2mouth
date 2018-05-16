def w1(fun):
	def inner(*args,**kwargs):
		print('验证')
		ret = fun(*args,**kwargs)
		return ret
	return inner
@w1
def test(a,b):
	print('a = %d , b = %d'%(a,b))
	return '哈哈啊哈哈哈'
print(test(1,2))
 

