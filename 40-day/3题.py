def w(cls):
	_instance = {}
	def w1(*args,**kwargs):
		if cls not in _instance:
			_instance[cls] = cls(*args,**kwargs)
		return _instance[cls]
	return w1

@w
class A(object):
	a = 1
	def __init__(self,x = 0):
		self.x = x
dog = A(2)
print(dog.x)
dog1 =A(4)
print(dog1.x) 
print(id(dog))
print(id(dog1))
