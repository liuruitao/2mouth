import os

ret = os.fork()

if ret == 0:
	print('我是子进程')
else:
	print('我是父进程')

