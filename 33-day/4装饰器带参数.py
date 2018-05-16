def w2(p):  #返回@w1
	def w1(fun):	
		def inner(*args,**kwargs):
			if p == 'lala':
				print('验证test')
			elif p == 'woca':
				print('验证test1')
			elif p == 'xixi':
				print('验证test2')
			elif p == 'huohuo':
				print('验证test3')
			ret = fun(*args,**kwargs)
			return ret
		return inner
	return w1
@w2('lala')  #相当于@w1
def test(a,b):
	print('a = %d , b = %d'%(a,b))
	return '哈哈啊哈哈哈'
@w2('woca')
def test1():
	print('天空飘来五个字')
@w2('xixi')
def test2(a,b):
	print('卧槽我在拔刀')
@w2('huohuo')
def test3():
	return '略略略'
test1()
test2(1,2)
print(test3())
print(test(1,2))
 

