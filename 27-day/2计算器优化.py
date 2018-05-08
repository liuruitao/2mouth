class OP(object):
	def __init__(self,num1,num2):
		self.num1 = num1
		self.num2 = num2
	def getResult(self):
		pass
class Jia(OP):
	def getResult(self):
		return self.num1 + self.num2
class Jian(OP):
	def getResult(self):
		return self.num1 - self.num2
class Cheng(OP):
	def getResult(self):
		return self.num1 * self.num2
class Chu(OP):
	def getResult(self):
		if self.num2 != 0:
			return self.num1 / self.num2
j = Jia(6,2)
print(j.getResult())
a = Jian(6,2)
print(a.getResult())
b = Cheng(6,2)
print(b.getResult())
c = Chu(6,2)
print(c.getResult())
