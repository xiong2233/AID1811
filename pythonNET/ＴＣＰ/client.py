#tcp_client.py

from socket import *
from time import *
#创建套接字
sockfd = socket()
#发起连接请求
server_addr = ('127.0.0.1',8888)
sockfd.connect(server_addr)
#消息收发
while True:
    data = input(">>")
    if not data:
        break
    sockfd.send(data.encode())
    sleep(2)
    data = sockfd.recv(1024)
    print("From server:",data.decode())
    
    
#关闭
sockfd.close()