from socket import *

s = socket(AF_INET,SOCK_DGRAM)

s.sendto('zz'.encode('gb2312'),('192.168.1.116',8080))

s.close()
