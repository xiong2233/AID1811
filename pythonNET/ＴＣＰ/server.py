#tcp_server.py
import socket
#创建套接字
sockfd = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#绑定地址
sockfd.bind(('127.0.0.1',8888))
#设置监听
sockfd.listen(5)
#等待处理客户端连接
while True:
    print('Waiting for connect..')
    connfd,addr = sockfd.accept()
    print("Connect from",addr) #打印客户端地址
    while True:
        #消息收发
        #客户端退出立即返回空字串
        data = connfd.recv(1024)
        if not data:
            break
        print("Recive Msg:",data.decode())
        n = connfd.send(b'I see')
        print("send %d bytes" %n)
    #关闭套接字
    connfd.close()
sockfd.close()
#cd aid1811/pythonNET