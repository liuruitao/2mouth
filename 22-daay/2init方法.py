class Boy():
	def __init__(self,age,height,weight):
		self.age = age
		self.height = height
		self.weight = weight
		self.address = "河北"
		self.games = []
	def study(self):
		print("热爱学习")
	def open_car(self,car):
		print("会开车%s"%car)
	def showage(self):
		print("年龄是%s"%self.age)
	def addgames(self,game):
		self.games.append(game)
		#print("爱玩的游戏是:%s"%game)
	def showgames(self):
		for i in self.games:
			print(i)
#a = input("请输入玩的游戏:")
#a.self.games
lrt = Boy(20,177,120)
lrt.study()
lrt.open_car("奥迪")
lrt.showage()
lrt.addgames("dnf,cf")
lrt.showgames()
