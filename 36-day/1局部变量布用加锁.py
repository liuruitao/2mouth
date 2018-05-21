from threading import Thread
import time
import threading

def work():
	name = threading.current_thread().name
	print(name)
	num = 1
	num+=1
	time.sleep(1)
	print('啦啦啦啦啦%d'%num)

def work1():
	name = threading.current_thread().name
	print(name)
	time.sleep(2)
	num = 10
	print('略略略略略%d'%num)

t = Thread(target = work)
t.start()

t1 = Thread(target = work1)
t1.start()
