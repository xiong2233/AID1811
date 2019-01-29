from socket import *
import pymysql
import os
import sys
import time
import signal



#定义全局变量
Host = '0.0.0.0'
Port = 8000
ADDR = (Host,Port)
DICT_TEXT = './dict.txt'


#创建子进程连接
def main():
    #创建数据库
    db = pymysql.connect("localhost","root","123456",'dict')
    
    #创建套接字
    sockfd = socket()
    sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    sockfd.bind(ADDR)
    sockfd.listen(5) 
    print("Listen to the port 8888...")  

    #处理僵尸进程
    signal.signal(signal.SIGCHLD,signal.SIG_IGN)
 
    #循环接受连接
    while True:
        try:
            c,addr = sockfd.accept()
        except KeyboardInterrupt:
            c.close()
            sys.exit("退出服务器")
        except Exception as e:
            print("连接失败",e)
            continue
        print("连接客户端",addr)
        #创建子进程
        pid = os.fork()
        if pid == 0:
            sockfd.close()
            do_child(c,db)
            os._exit(0)
        else:
            c.close()

def do_child(c,db):
    while True:
        data = c.recv(128).decode()
        print(c.getpeername(),':',data)
        if (not data) or data[0] =='Q':
            c.close()
            sys.exit()
        elif data[0]=='R':
            do_register(c,db,data)
        elif data[0] == 'E':
            do_login(c,db,data)
        elif data[0] == 'Q':
            return
        elif data[0] == 'F':
            do_find(c,db,data)
        elif data[0] == 'H':
            do_hist(c,db,data)
#注册
def do_register(c,db,data):
    l = data.split(" ")
    name = l[1]
    passwd = l[2]
    cursor = db.cursor()
    sql = '''select * from user where name='%s'
    '''%name
    cursor.execute(sql)
    r = cursor.fetchone()
    if r != None:
        c.send(b"EXISTS")
        return
    #插入用户
    sql = "insert into user(name,password) values('%s','%s')"%(name,passwd)
    try:
        cursor.execute(sql)
        db.commit()
        c.send(b'ok')
    except Exception as e:
        db.rollback()
        c.send(b"FAIL")
        print(e)

def do_login(c,db,data):
    l = data.split(" ")
    name = l[1]
    passwd = l[2]
    cursor = db.cursor()
    sql ="select * from user  where name='%s' "%name
    cursor.execute(sql)
    r = cursor.fetchone() 
    if r == None:
        c.send(b"FAIL")
        return
    else:
        sql = "select password from user where name='%s'"%name
        cursor.execute(sql)
        x = cursor.fetchone()[0]
        if str(x) == passwd:
            c.send(b"ok")
        else:
            c.send(b"ERROR")

def do_find(c,db,data):
    l = data.split(" ")
    word = l[1]
    name = l[2]
    if word == '##':
        c.send(b"CLOSE")
        print("退出字典")
        return
    cursor = db.cursor()
    sql = "select interpret from words where word='%s'"%word
    cursor.execute(sql)
    r = cursor.fetchone()
    if r == None:
        c.send(b"NONE")
    else:
        c.send(r[0].encode())
    sql = "insert into hist(name,word,time) values('%s','%s','%s')"%(name,word,str(time.ctime()))
    try:
        cursor.execute(sql)
        db.commit()
        print("传输成功")
    except Exception as e:
        db.rollback()
        print(e)

def do_hist(c,db,data):
    l = data.split(" ")
    name = l[1]
    cursor = db.cursor()
    sql = "select * from hist where name='%s' order by id desc limit 10"%name
    cursor.execute(sql)
    r = cursor.fetchall()
    print(r)
    if r == None:
        print("没有历史记录")
        c.send("None")
    for i in r:
        msg = i[1] +' ' +i[2] + ' ' +i[3]
        c.send(msg.encode())
        time.sleep(0.2)
    time.sleep(0.5)
    c.send(b"##")


    
main()
        


