"""
HTTP Server v2.0
多线程并发
可以做ｒｅｑｕｅｓｔ解析
能够返回简单的数据
使用类进行封装
"""

from socket import *
from threading import Thread
import sys

#httpserver主体功能
class HTTPServer(object):
    def __init__(self,addr,static_dir):
        self.server_address = addr
        self.static_dir = static_dir
        self.ip = addr[0]
        self.port = addr[1]
        #创建套接字
        self.create_socket()
    #创建套接字
    def create_socket(self):
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
        self.sockfd.bind(self.server_address)
    
    def Server_forever(self):
        self.sockfd.listen()
        print("Listen to the port %d"%self.port)
        while True:
            try:
                connfd,addr = self.sockfd.accept()
            except KeyboardInterrupt:
                self.sockfd.close()
                sys.exit("服务器退出")
            except Exception as e:
                print("Error",e)
                continue
            #创建线程处理客户端请求
            clientThread = Thread(target=self.handle,args=(connfd,))
            clientThread.setDaemon(True)
            clientThread.start()

    def handle(self,connfd):
        #接收http请求
        request = connfd.recv(4096)
        if not request:
            connfd.close()
            return
        #按行切割
        request_lines = request.splitlines()
        print(connfd.getpeername(),':',request_lines[0])
        #获取具体请求
        getRequest = str(request_lines[0]).split(' ')[1]
        print(getRequest)
        if getRequest == '/' or getRequest[-5:] == '.html':
            self.get_html(connfd,getRequest)
        else:
            self.get_data(connfd,getRequest)
        connfd.close()
    def get_data(self,connfd,getRequest):
        urls = ['/time','/tedu','/hello']
        if getRequest in urls:
            responseHanders='HTTP/1.1 200 ok\r\n'
            responseHanders+='\r\n'
            if getRequest =='/time':
                import time
                responseBody = time.ctime()
            elif getRequest == '/tedu':
                responseBody="Tedy Python"
            elif getRequest =='/hello':
                responseBody="hello world"
        else:
            responseHanders='HTTP/1.1 404 Not found\r\n'
            responseHanders+='\r\n'
            responseBody="Sorry No data"
        response=responseHanders+responseBody
        connfd.send(response.encode())

    #发送网页给客户端
    def get_html(self,connfd,getRequest):
        if getRequest == '/':
            filename = self.static_dir + '/index.html'
        else:
            filename = self.static_dir + getRequest
        try:
            f = open(filename)
        except Exception:
            #没有找到网页
            responseHanders = 'HTTP/1.1 404 Not found\r\n'
            responseHanders += '\r\n'
            responseBody = '<h1>Sorry Not found the page</h1><hr>'
            print("se")
        else:
            responseHanders = 'HTTP/1.1 200 ok\r\n'
            responseHanders += '\r\n'
            responseBody = f.read()
        finally:
            response = responseHanders + responseBody
            connfd.send(response.encode())


if __name__ == '__main__': #?
    #用户自己确定
    server_addr = ("0.0.0.0",8000)
    static_dir = './static'  #存放网页
    #创建服务器对象
    httpd = HTTPServer(server_addr,static_dir)
    #启动http server
    httpd.Server_forever()
