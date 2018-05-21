from threading import Thread
import time
import threading

class work(Thread):
	def run(self):
		if mutexA.acquire():
			print(self.name+'---do1--up---')
			time.sleep(1)
			
			if mutexB.acquire():
				print(self.name+'---do1---down---')
				mutexB.release()	
			mutexA.release()

class work1(Thread):
	def run(self):
		if mutexB.acquire():
			print(self.name+'---do2--up---')
			time.sleep(1)
			
			if mutexA.acquire():
				print(self.name+'---do2---down---')
				mutexA.release()	
			mutexB.release()

mutexA = threading.Lock()
mutexB = threading.Lock()

t = work()
t1 = work1()
t.start()
t1.start()

