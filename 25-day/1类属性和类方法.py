class Dog(object):
	name = '泰日天'
	def run(self):
		print('跑')
	def eat(self):
		print('吃骨头')
	@classmethod
	def getname(cls):
		return cls.name

ritian = Dog()
ritian.run()
ritian.eat()
print(Dog.getname())
print(ritian.getname())
