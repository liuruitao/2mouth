class property():
	def eat(self):
		print("吃狗粮")
	def play(self):
		print("玩弹力球")
	def introduce(self):
		print("我的品种是:%s\n我的名字是:%s\n我的颜色是:%s\n我的年龄是:%d"%(self.breed,self.name,self.color,self.age))
erha = property()
erha.breed = "哈士奇"
erha.name = "肸肸"
erha.color = "黑白色"
erha.age = 2
erha.eat()
erha.play()
erha.introduce()

jinmao = property()
jinmao.breed = "金毛"
jinmao.name = "健健"
jinmao.color = "棕色"
jinmao.age = 1
jinmao.eat()
jinmao.play()
jinmao.introduce()

taidi = property()
taidi.breed = "泰迪"
taidi.name = "日天"
taidi.color = "白色"
taidi.age = 2
taidi.eat()
taidi.play()
taidi.introduce()


