from threading import Thread,Lock
import time

class work(Thread):
	def run(self):
		while True:	
			if lock1.acquire():
				print('---work---')
				time.sleep(0.5)
				lock2.release()

class work1(Thread):
	def run(self):
		while True:	
			if lock2.acquire():
				print('---work1---')
				time.sleep(0.5)
				lock3.release()

class work2(Thread):
	def run(self):
		while True:	
			if lock3.acquire():
				print('---work2---')
				time.sleep(0.5)
				lock1.release()

lock1 = Lock()

lock2 = Lock()
lock2.acquire()

lock3 = Lock()
lock3.acquire()

t = work()
t1 = work1()
t2 = work2()

t.start()
t1.start()
t2.start()

