from socket import *

s = socket(AF_INET,SOCK_DGRAM)

#先绑定端口,在发送和接受信息
s.bind(('',4567))

s.sendto("哈哈".encode("gb2312"),("192.168.1.111",8080))

while True:
	content,info = s.recvfrom(1024)

	print("%s----%s"%(content.decode("gb2312"),info[0]))
s.close()

