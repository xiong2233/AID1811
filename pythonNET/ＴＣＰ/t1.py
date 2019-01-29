from socket import *
# 1.创建套接字
sockfd = socket() #默认为流式套接字

sockfd.bind(('0.0.0.0',8886))

sockfd.listen(5)

connfd,addr=sockfd.accept()

connfd.recv(1024)
connfd.send('ok'.encode())
print("结束")
connfd.close()
sockfd.close()