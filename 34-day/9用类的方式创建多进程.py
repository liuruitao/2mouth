from multiprocessing import Process
import time

class Dog(Process):
	def __init__(self,name):
		Process.__init__(self)
		self.name = name
	
	#一定要重写run方法  run固定
	def run(self):
		for i in range(5):
			if self.name == 'a':
				time.sleep(1)
				print('乐乐是狗')
			elif self.name == 'b':
				time.sleep(1)
				print('乐乐是猫')
		
cat = Dog('b')
dog = Dog('a')
cat.start()
dog.start()
cat.join()
dog.join()
