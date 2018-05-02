class Home():
	def __init__(self,area,price,hometype,address):
		self.area = area
		self.price = price
		self.hometype = hometype
		self.address = address
		self.list = []
	def __str__(self):
		return "房子的面积是:%d平\n房子的价格是:%d万\n房子的户型是:%s\n房子的地址是:%s"%(self.area,self.price,self.hometype,self.address)
	def AddBed(self,Bed):
		self.list.append(Bed)
		print("添加成功")
	def AddLamp(self,Lamp):
		self.list.append(Lamp)
		print("添加成功")
class Bed():
	def __init__(self,area,price,bedtype):
		self.area = area
		self.price = price
		self.bedtype = bedtype
	def __str__(self):
		return "床的面积是:%d平\n床的价格是:%d万\n床的类型是:%s"%(self.area,self.price,self.bedtype)
class Lamp():
	def __init__(self,limit,price):
		self.limit = limit
		self.price = price
	def __str__(self):
		return "灯的度数是:%s瓦\n灯的价格是:%s元"%(self.limit,self.price)
def Open():
	print("房间亮了")
def Close():
	print("房间灭了")
myhome = Home(120,1200,"三室一厅","北京市五环")
print(myhome)
mybed = Bed(4,2,"席梦思")
print(mybed)
myhome.AddLamp(mybed)
mylamp = Lamp(500,1000)
print(mylamp)
myhome.AddBed(mylamp)
switch = input("请选择开关:")
if switch == "开":
	Open()
elif switch == "关":
	Close()
