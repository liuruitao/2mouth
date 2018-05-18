from threading import Thread
import time

def sing():
	for i in range(3):
		time.sleep(1)
		print('阿拉拉拉拉拉阿拉啦啦')

def dance():
	for i in range(3):
		time.sleep(1)
		print('蹦擦擦蹦擦擦蹦擦擦')

t = Thread(target=sing)
t1 = Thread(target=dance)

t.start()
t1.start()
