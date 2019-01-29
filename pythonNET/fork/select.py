#导入数据库
from select import select
from socket import *
import sys
from time import ctime
#创建套接字
s = socket()
#设置套接字?
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
#绑定地址
s.bind(("0.0.0.0",8888))
#监听连接
s.listen(5)
#导入标准输入流
t = sys.stdin
#打开文件，以只写方式
fd = open("the.txt",'a')

#设置ｓｅｌｅｃｔ参数，并加入监听和输入
rlist = [s,t]
wlist = []
xlist = [s,t]
while True:
    #io多路复用，检测ｓ或ｔ
    rs,ws,xs = select(rlist,wlist,xlist)
    #检测rlist
    for r in rs:
        #判断是否为ｔ
        if r is t:
            txt = t.readline()
            txt = ctime() +' '+ txt
            print(txt)
            fd.write(txt)
        else:
            if r is s:
                c,addr = r.accept()
                print("Connect from",addr)
                rlist.append(c)

            else:
                data = r.recv(1024)
                if not data:
                    rlist.remove(r)
                    r.close()
                    continue
                print("Receive from %s:%s"%(r.getpeername(),data.decode()))   
                fd.write(ctime(),data.decode()) 
                f.flush()
                # r.send(b'receive')
                wlist.append(r)
    for w in ws:
        w.send(b'recv your msg')
        wlist.remove(w)
    for x in xs:
        x.close()
        raise