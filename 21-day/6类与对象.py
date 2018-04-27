class People:
	def eat(self):
		print("吃东西")
	def sleep(self):
		print("睡觉")
LRT = People()
LRT.weight = 120
LRT.height = 177
LRT.eat()
LRT.sleep()
print(LRT.weight)
print(LRT.height)
