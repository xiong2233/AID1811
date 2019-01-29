from socket import *
import sys
#从命令行传入ＩＰ　ｐｏｒｔ
host = sys.argv[1]
port = int(sys.argv[2])
addr = (host,port)
#创建套接字
sockfd = socket(AF_INET,SOCK_DGRAM)
#接收发消息
while True:
    data = input(">>")
    if not data:
        break
    sockfd.sendto(data.encode(),addr)
    msg,addr = sockfd.recvfrom(1024)
    print("接收消息为：",msg)
sockfd.close()
