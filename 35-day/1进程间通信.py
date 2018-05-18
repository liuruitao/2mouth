from multiprocessing import Process,Queue
import os,time,random

def write(q):
	for i in ['我曹','我在','拔刀']:
		print('获取%s消息'% i)
		q.put(i)
		time.sleep(random.random())

def read(q):
	while True:
		if not q.empty():
			i = q.get(True)
			print('拿出并删除%s消息'% i)
			time.sleep(random.random())
		else:
			break

if __name__ == '__main__':
	q = Queue()
	pw = Process(target=write, args=(q,))
	pr = Process(target=read, args=(q,))
	pw.start()
	pw.join()
	pr.start()
	pr.join()
	print('所有数据都写入并读取完')

