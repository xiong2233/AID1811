from socketserver import *

#创建服务器类
class Server(ForkingMixIn,TCPServer):       #多进程
# class Server(ThreadingMixIn,TCPServer):   #多线程
# class Server(ForkingTCPServer):
# class Server(ThreadingTCPServer):
    pass

#具体请求处理类
class Handler(StreamRequestHandler):
    def handle(self):
        print("Connect from",self.client_address)
        while True:
            #self.request就是ａｃｃｅｐｔ返回的套接字
            data = self.request.recv(1024)
            if not data:
                break
            print(data.decode())
            self.request.send(b'ok')

#创建服务器对象,绑定处理
server_addr = ('0.0.0.0.',8888)
server =Server(server_addr,Handler)
server.serve_forever()  #启动服务

