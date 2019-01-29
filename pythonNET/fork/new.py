from socket import * 
import os,sys
import time 

class FtpServer():
    def __init__(self,connfd):
        self.connfd = connfd
    def do_list(self):
        print("执行List")
        #获取文件列表
        file_list = os.listdir(FILES)
        #文件库目录为空则不许获取
        if not file_list:
            self.connfd.send("文件库为空")
            return
        else:
            self.connfd.send(b'ok')
            time.sleep(0.1)

        files = ''
        for file in file_list:
            if file[0] != '.' and os.path.isfile(FILES + file):
                files = files + file + '#'
        #将拼接好的文件字符串发送
        self.connfd.send(files.encode())
    def do_get(self,filename):
        try:
            fd = open(FILES+filename,'rb')
        except Exception:
            self.connfd.send("文件不存在".encode())
            return 
        self.connfd.send(b'ok')
        time.sleep(0.1)
        while True:
            data = fd.read(1024)
            if not data:
                time.sleep(0.1)
                self.connfd.send(b'##')
                break
            self.connfd.send(data)
    
    def do_put(self,filename):
        try:
            fd = open(FILES+filename,'wb')
        except:
            self.connfd.send("上传失败")
        else:
            self.connfd.send(b'ok')
        while True:
            data = self.connfd.recv(1024)
            if data == b'##':
                break
            fd.write(data)
        fd.close()
        print("文件接受完毕")

            



        
#全局变量
HOST = '0.0.0.0'
PORT = 8888
ADDR = (HOST,PORT)
FILES = '/home/tarena/abc/'

#封装并发网络模型
def main():
    #创建套接字
    sockfd = socket()
    sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    sockfd.bind(ADDR)
    sockfd.listen(5) 
    print("Listen to the port 8888...")  
    #循环接受连接
    while True:
        try:
            connfd,addr = sockfd.accept()
        except KeyboardInterrupt:
            connfd.close()
            sys.exit("退出服务器")
        except Exception as e:
            print("连接失败",e)
            continue
        print("连接客户端",addr)
        #创建子进程
        pid = os.fork()
        if pid == 0:
            #创建二级子进程
            p = os.fork()
            if pid == 0:
                sockfd.close()
                ftp = FtpServer(connfd)#创建对象
                while True:
                    data = connfd.recv(1024).decode()
                    if not data or data[0] == 'Q':
                        sys.exit("客户端退出")
                    elif data[0] == 'L':
                        ftp.do_list()
                    elif data[0] == 'G':
                        filename = data.split(" ")[-1]
                        ftp.do_get(filename)
                    elif data[0] == 'P':
                        filename = data.split(" ")[-1]
                        ftp.do_put(filename)
            else:
                os._exit(0)#关闭一级子进程
        else:
            connfd.close()
            os.wait()   #接收等待一级子进程结束
main()
    