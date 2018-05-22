from socket import *

s = socket(AF_INET,SOCK_DGRAM)

content = "1:123123:lw:lw-pc:32:hehehe"
s.sendto(content.encode("gb2312"),("172.16.75.1",2425))

s.close()

