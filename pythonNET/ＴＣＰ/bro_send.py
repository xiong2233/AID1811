from socket import * 
from time import sleep
#设置广播目标格式
dest = ('176.221.15.255',8666)
s = socket(AF_INET,SOCK_DGRAM)
s.setsockopt(SOL_SOCKET,SO_BROADCAST,1)
while True:
    sleep(2)
    s.sendto('往后余生，风雪是你'.encode(),dest)
s.close()