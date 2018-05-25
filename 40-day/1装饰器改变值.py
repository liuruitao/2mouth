def w(cls):
	def w1(*args,**kwargs):
		return cls(3)
	return w1

@w
class Dog(object):
	def __init__(self,x = 0):
		self.x = x

dog = Dog(1)
print(dog.x)

