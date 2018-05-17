from multiprocessing import Pool
import os,time
#子进程
def work(msg):
	for i in range(3):
		time.sleep(1)
		print('略略略略略pid=%d'%os.getpid())

p = Pool(1)
#主进程
for i in range(1,6):
	print(i)
	p.apply(work,(i,))

p.close()  #关闭池子
p.join()  #等待p中所有子进程执行完,必须放在close语句后

