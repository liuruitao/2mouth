class  Pen():
	def __init__(self):
		self.__money = 100
	def getmoney(self):
		return self.__money
	def setmoney(self,money):
		if money <= 0:
			print("MMP")
		else:
			self.__money = money
xiaoming = Pen()
xiaoming.setmoney(-300)
print(xiaoming.getmoney())
