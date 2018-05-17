from multiprocessing import Process
#import os
import time

def test(name):
	for i in range(5):
		time.sleep(1)
		print('阿达阿达阿达,名字%s'%name)
	
p = Process(target= test,args=('lrt',))
print('打不着打不着')
p.start()
time.sleep(2)
p.join(3)
print('略略略')
