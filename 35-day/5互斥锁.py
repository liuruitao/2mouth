from threading import Thread,Lock
import time

num = 0

def work():
	global num
	mutex.acquire()  #mutex非固定值
	for i in range(1000000):
		num+=1
	print('经线程1修改后全局变量是:%d'%num)
	mutex.release()

#多线程共享全局变量,变量num经work改变后共享给work1
def work1():
	global num
	mutex.acquire()
	for i in range(1000000):
		num+=1
	print('经线程2修改后全局变量是:%d'%num)
	mutex.release()

print('线程创之前全局变量是:%d'%num)

mutex = Lock()

t1 = Thread(target=work)
t1.start()

t2 = Thread(target=work1)
t2.start()
