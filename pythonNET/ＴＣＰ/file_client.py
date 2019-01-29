from socket import *
sockfd = socket()
sockfd.connect(('127.0.0.1',8855))
fd = open('t1.jpg','rb')
while True:
    try:
        txt = fd.read(1024)
        if not txt:
            break
        sockfd.send(txt)
        data = sockfd.recv(1024)
        print(data.decode())
    except Exception as e:
        print('出错了',e)
fd.close()
sockfd.close()