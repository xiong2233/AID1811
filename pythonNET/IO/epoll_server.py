from select import *
from socket import *
#创建套接字
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(("0.0.0.0",9966))
s.listen(3)

#创建ｐｏｌｌ对象
p = epoll()

#建立查找字典
fdmap = {s.fileno():s}

#注册关注ｉｏ
p.register(s,EPOLLIN|EPOLLERR)

while True:
    events = p.poll()   #监控ｉｏ
    for fd,event in events:
        if fd == s.fileno():
            c,addr = fdmap[fd],accept()
            print("Connect from",addr)
            #添加新的关注事件
            p.register(s,EPOLLIN|EPOLLHUP)
            fdmap[c.fileno()] = c
            #通过按位与判断某个事件是否就绪
        elif event & EPOLLIN:
            data =fm[fd].recv(1024)
            if not data:
                #客户端退出，则取消关注
                p.unregister(fd)
                fdmap[fd].close()
                del fdmap[fd]
            else:
                print("Receive",data.decode())
                fdmap[fd].send(b'Recive')