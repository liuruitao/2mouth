import os

ret = os.fork()

#父进程的ret就是子进程的pid
#父进程的pid就是子进程的ppid
if ret == 0:
	print('我是子进程, %d, pid=%d, ppid=%d'%(ret,os.getpid(),os.getppid()))
else:
	print('我是父进程, %d, pid=%d, ppid=%d'%(ret,os.getpid(),os.getppid()))

