class Money(object):
	def __init__(self):
		self.__money = 0

	@property
	def money(self):
		return self.__money

	@money.setter
	def money(self,value):
		if isinstance(value,int):
			self.__money = value
		else:
			print('error:不是整数型')

maoyeye = Money
maoyeye.money = 226.3226
print(maoyeye.money)
