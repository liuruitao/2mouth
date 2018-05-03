import time
class Dog():
	def __init__(self,name):
		self.__name = name
	def __del__(self):
		print('干掉')
dog = Dog("txn")
del dog
time.sleep(2)
a = Dog
b = a
c = a
print("删a")
del a
time.sleep(2)
print('删b')
del b
time.sleep(2)
print('删c')
del c
time.sleep(2)
