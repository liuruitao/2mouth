import os

num = 0

ret = os.fork()

#fork炸弹
#while True:
#	os.fork()

#子进程和父进程的变量各不一样
if ret == 0:
	num+=1
	print('我是子进程, num=%d'%num)
else:
	num+=2
	print('我是父进程, num=%d'%num)

