class Father(object):
	def __init__(self):
		self.__girl_count = 4
	def getgirl_count(self):
		return self.__girl_count
	def money(self):
		print('我会挣钱')
	def Run(self):
		print('我会跑步')
	def __speak(self):
		print('我会吹牛逼')
	def setspeak(self):
		self.__speak()
class Son(Father):
	pass
xiaoliang = Son()
xiaoliang.money()
xiaoliang.Run()
print(xiaoliang.getgirl_count())
xiaoliang.setspeak()
