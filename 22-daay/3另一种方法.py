class Boy():
	def __init__(self,age,height,weight):
		self.age = age
		self.height = height
		self.weight = weight
		self.address = "河北"
		self.games = []
		self.a = input("请输入爱玩的游戏:")
		self.games.append(self.a)
		for i in self.games:
			print("爱玩的游戏是:"+i)
	def study(self):
		print("热爱学习")
	def open_car(self,car):
		print("会开上%s"%car)
lrt = Boy(20,177,120)
print("今年%s\n身高%s\n体重%s"%(lrt.age,lrt.height,lrt.weight))
lrt.study()
lrt.open_car("奥迪")
