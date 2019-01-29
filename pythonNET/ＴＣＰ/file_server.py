from socket import *
sockfd = socket()
sockfd.bind(('127.0.0.1',8855))
sockfd.listen(5)
connfd,addr = sockfd.accept()
print("已连接地址：",addr)
fr = open('image.jpg','wb')
while True:
    data = connfd.recv(1024)
    if not data:
        break
    fr.write(data)
    connfd.send('ok'.encode())
connfd.close()
sockfd.close()
