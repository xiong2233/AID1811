from select import *
from socket import *
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.0',9966))
s.listen(3)

p = epoll()

fdmap = {s.fileno():s}

p.register(s,EPOLLIN|EPOLLERR)

while True:
    events = p.poll()
    for fd,event in events:
        if fd == s.fileno():
            c,addr = fdmap[fd].accept()
            print("连接的客户端地址为：",addr)
            p.register(c,EPOLLIN|EPOLLHUP|EPOLLET)  #添加边缘触发
            fdmap[c.fileno()] = c
        elif event & EPOLLIN:
            data = fdmap[fd].recv(1024)
            if not data:
                break
                p.unregister(fd)
                fdmap[fd].close()
                del fdmap[fd]
            else:
                fdmap[fd].send("已收到".encode())
                print(data.decode())