from select import select
from socket import *

#准备要关注的ｉｏ
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.0',8888))
s.listen(3)

#添加关注列表
rlist=[s]
wlist=[]
xlist=[]

while True:
    #监控ｉｏ的发生
    rs,ws,xs = select(rlist,wlist,xlist)
    #遍历三个列表，确定那个ｉｏ发生
    for r in rs:
        #如果遍历到ｓ说明ｓ就绪则有客户端发起连接
        if r is s:
            c,addr = r.accept()
            print("Connect from",addr)
            rlist.append(c)
        #客户端连接套接字就绪，则接收消息
        else:
            data = r.recv(1024)
            if not data:
                #客户端退出从关注列表移出
                rlist.remove(r)
                r.close()
                continue
            print("Receive from %s:%s"%(r.getpeername(),data.decode()))
            # r.send(b'receive')
            wlist.append(r)
    for w in ws:
        w.send(b'recv your msg')
        wlist.remove(w)
    for x in xs:
        x.close()
        raise