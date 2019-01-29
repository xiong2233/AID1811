from socket import *
#创建ｕｄｐ套接字
sockfd = socket(AF_INET,SOCK_DGRAM)
#绑定地址
sockfd.bind(('127.0.0.1',8888))
#接收发消息
while True:
    data,addr= sockfd.recvfrom(1024)
    print('内容：',data.decode(),'地址：',addr)
    sockfd.sendto(b'ok',addr)
    print("已发送")
#关闭套接字
sockfd.close()
