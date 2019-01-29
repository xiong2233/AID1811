from socket import *
import sys
import multiprocessing import Process 
import signal #信号处理模块
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
    sys.exit(0)  #客户端子进程也退出
#创建套接字   
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(("0.0.0.0",8888))
s.listen(3)

#忽略子进程退出释放资源请求，交由系统处理
signal.signal(signal.SIGCHLD,signal.SIG_IGN)

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
p = Process(target=handler,args=(c,))
p.daemon = True
p.start()
