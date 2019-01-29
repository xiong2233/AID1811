from select import *
from socket import *
#创建套接字
s = secket()
#使地址可以重复使用
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
#绑定地址
s.bind(('0.0.0.0',9966))
#监听
s.listen(3)

#创建poll对象
p = poll()
#创建字典,放入服务器套接字的文件描述符及相关信息
fdmap = {s.fileno():s}

#注册关注ｉｏ为服务器,设定关注事件为
p.register(s,POLLIN|POLLERR)

while True:
    events = p.poll() #监控ｉｏ（第一次监控的对象为服务器）
    for fd,event in events:  #第一次events为[(服务器文件描述符，事件)]
        if fd == s.fileno():    #判断 文件描述符是否为服务器文件描述符
            c,addr = fdmap[fd].accept() #服务器与客户端进行连接　等同于　s.accept()
            print("客户端地址：",addr)  #打印客户端地址
            p.register(c,POLLIN|POLLHUP) #注册关注现连接客户端，关注事件为读取输入及断开连接
            fdmap[c.fileno()] = c  #将现客户端的文件描述符及相关信息加入字典
        elif event & POLLIN:        #有事件发生并且是读取输入事件
            data = fdmap[fd].recv(1024)  #接收消息
            if not data:        #如果没有消息及客户端断开连接
                break
                p.unregister(fd)  #取消关注当前客户端
                fdmap[fd].close()   #关闭当前客户端与服务器的连接
                del fdmap[fd]   #删除字典中存有的当前客户端
            else:
                print("客户端发送的是：",data.decode())  #打印接收的内容
                fdmap[fd].send(b"ok")　　#给客户端发送消息


        





