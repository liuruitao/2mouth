from multiprocessing import Process
#import os
import time

def test(name):
	for i in range(5):
		time.sleep(1)
		print('阿达阿达阿达,名字%s'%name)
	
def test1(name):
	for i in range(5):
		time.sleep(1)
		print('阿擦阿擦阿擦,名字%s'%name)
	
p = Process(target= test,args=('lrt',))
p1 = Process(target= test1,args=('lrt',))
print('打不着打不着')
p.start()
p1.start()
time.sleep(2)
p.join()  #超时时间
p1.join()  #超时时间
print('略略略')
