def w1(fun):
	def inner():
		print('验证')
		fun()
	return inner
@w1
def test():
	print('略略略')


#test = w1(test)
test()
