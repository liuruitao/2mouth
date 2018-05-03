class Father(object):
	def makeMoney(self):
		print('用双手赚钱')


class Son(Father):
	def makeMoney(self):
		print('用脑子')
		super().makeMoney()
lrt = Son()
lrt.makeMoney()
