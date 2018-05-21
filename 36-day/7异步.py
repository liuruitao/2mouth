from multiprocessing import Pool
import time 

def test1():
	for i in range(3):
		print('饭好了叫我')
		time.sleep(0.5)
	return '饭好了'

def test2(args):
	print(args)
	print('来了')

p = Pool()
p.apply_async(func=test1,callback=test2)
#while True:
for i in range(3):
	time.sleep(1)
	print('写作业中')
