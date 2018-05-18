from threading import Thread
import time

num = 0

def work():
	global num
	for i in range(1000000):
		num+=1
	print('经线程1修改后全局变量是:%d'%num)
#多线程共享全局变量,变量num经work改变后共享给work1
def work1():
	global num
	for i in range(1000000):
		num+=1
	print('经线程2修改后全局变量是:%d'%num)

print('线程创之前全局变量是:%d'%num)
t1 = Thread(target=work)
t1.start()
time.sleep(1)
t2 = Thread(target=work1)
t2.start()
