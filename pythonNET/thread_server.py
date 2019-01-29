from socket import *
import sys
import threading import Thread
#客户端
def handler(c):
    print("Connect from ",c.getpeername())
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
        s.send(b'Thank you')
    c.close()
#创建套接字   
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(("0.0.0.0",8888))
s.listen(3)

while True:
    try:
        c,addr = s.accept()
    except KeyboardInterrupt:
        s.close()
        sys.exit("服务器退出")
    except Exception as e:
        print("服务端异常",e)
        continue
#创建线程
t = Thread(target=handler,args=(c,))
t.setDaemon(True)
t.start()
