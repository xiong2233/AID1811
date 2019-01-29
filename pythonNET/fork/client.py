from socket import *
import sys,os
import time
#具体请求功能
class FtpClient(object):
    def __init__(self,sockfd):
        self.sockfd = sockfd
    #查看文件列表
    def do_list(self):
        self.sockfd.send(b'L') #发送请求
        #等待回复
        data = self.sockfd.recv(128).decode()
        if data == 'ok':
            data = self.sockfd.recv(4096).decode()
            files = data.split("#")
            for file in files:
                print(file)
        else:
            print(data) #打印无法操作原因
    
    def do_quit(self):
        self.sockfd.send(b'Q')
        self.sockfd.close()
        sys.exit("谢谢使用")

    def do_get(self,filename):
        self.sockfd.send(('G '+filename).encode())
        data = self.sockfd.recv(128).decode()
        if data == 'ok':
            fd = open(filename,'wb')
            while True:
                data = self.sockfd.recv(1024)
                if data == b'##':
                    break
                fd.write(data)
            fd.close()
        else:
            print(data)

    def do_put(self,filename):
        try:
            fd = open(filename,'rb')
        except Exception:
            print("没有此文件")
            return
        # filename = filename.split('/')[-1]
        self.sockfd.send(('P ' + filename).encode())
        data = self.sockfd.recv(128).decode()
        if data == 'ok':
            while True:
                data = fd.read(1024)
                if not data:
                    time.sleep(0.1)
                    self.sockfd.send(b'##')
                    break
                self.sockfd.send(data)
            fd.close()
            print("上传完毕")
        else:
            print(data)




#网络连接
def main():
    if len(sys.argv)<3:
        print("argv is error")
        return 
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
    addr = (HOST,PORT)
    #创建套接字
    sockfd = socket()
    try:
        sockfd.connect(addr)
    except Exception as e:
        print("连接服务器失败",e)
        return 
    ftp = FtpClient(sockfd) #创建对象
    while True:
        print("\n-------- 命令选项 --------")
        print("---------- list ----------")
        print("-------- get file --------")
        print("-------- put file --------")
        print("--------- quite ----------")
        print("--------------------------\n")
        cmd = input("请输入指令")
        if cmd.strip() == 'list':
            ftp.do_list()
        elif cmd.strip() == 'quit':
            ftp.do_quit()
        elif cmd[:3] == 'get':
            filename = cmd.split(" ")[-1]
            ftp.do_get(filename)
        elif cmd[:3] == 'put':
            filename = cmd.split(" ")[-1]
            print(filename)
            ftp.do_put(filename)
        else:
            print("请输入正确命令")
        
main()