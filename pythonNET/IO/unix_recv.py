from socket import *
import os 
#如果文件存在
if os.path.exists("./sock"):
    os.remove("./sock")
#创建本地套接字
sockfd = socket(AF_UNIX,SOCK_STREAM)

#绑定套接字文件
sockfd.bind("./sock")

#监听
sockfd.listen(3)
 while True:
    c,addr = sockfd.accept()
    while True:
        data = c.recv(1024)
        if nat data:
            break
        print(data.decode())
    c.close()
sockfd.close()