class Pen():
	def __Name(self,name):
		self.name = 1
		self.name = name
		print("扣")
	def publicName(self,name):
		if name > 0:		
			self.__Name(name)
		else:
			print("失败")
lrt = Pen()
lrt.publicName(6)
