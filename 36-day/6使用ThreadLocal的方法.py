from threading import Thread
import threading

local_school = threading.local()

def process_student():
	std = local_school.student
	print('Hello,%s (in %s)'%(std,threading.current_thread().name))

def process_thread(name):
	local_school.student = name
	process_student()

t1 = Thread(target = process_thread,args=('laozhao',),name='Thread-A')
t2 = Thread(target = process_thread,args=('laozhai',),name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()
