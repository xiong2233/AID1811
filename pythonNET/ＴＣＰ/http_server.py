from socket import *
#执行函数中处理客户端请求
def handle(connfd):
    print("获取客户端地址：",connfd.getpeername())
    request = connfd.recv(4096) #获取ｈｔｔｐ请求
    request_lines = request.splitlines()
    #打印ｈｔｔｐ请求的每一行
    for line in request_lines:
        print(line)
    # #给浏览器客户端返回响应
    # data = '''HTTP/1.1 200 ok
    # Content-Encoding:gzip
    # Content-Type:text/html

    # <html lang='en'>
    # <meta charset="utf-8">
    # <h1>Welcome to tedu Python</h1>
    # <p>新年快乐！</p>
    # </html>
    # '''
    #给浏览器客户端返回响应
    try:
        f = open("hh.html")
    except IOError:
        response = 'HTTP/1.1 404 Not found\r\n'
        response += '\r\n'
        response += '===sorry not found page'
    else:
        response = "HTTP/1.1 200 ok\r\n"
        response += '\r\n'
        response += f.read()
    finally:
        #将结果发送给浏览器
        connfd.send(response.encode())

    
#在主函数里创建套接字
def main():
    sockfd = socket()
    sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    sockfd.bind(('0.0.0.0',8000))
    sockfd.listen(3)
    print("Listen yo the port 127.0.0.1")
    while True:
        connfd,addr = sockfd.accept()
        #处理客户端请求
        handle(connfd)
        connfd.close()
main()   
