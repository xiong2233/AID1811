from socket import *
import sys
import getpass
import time

def main():
    if len(sys.argv) < 3:
        print("argv is error")
        return
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
    addr = (HOST,PORT)
    s = socket()
    try:
        s.connect(addr)
    except Exception as e:
        print("连接失败",e)
        return
    while True:
        #一级界面
        print("========== Welcome　==========")
        print("***********1 注册 ***********")
        print("***********2 登录 ***********")
        print("***********3 退出 ***********")
        print("=============================")
        cmd = input("请输入指令>>")
        if cmd not in ['1','2','3']:
            print("请输入正确的选项")
            sys.stdin.flush() #清除标准输入
            continue
        elif cmd == '1':
            do_register(s) #注册
        elif cmd == '2':
            do_login(s) 
        elif cmd =='3':
            s.send(b"Q")
            return


def do_register(s):
    while True:
        name = input("User:")
        passwd = getpass.getpass("password：")
        passwd1 = getpass.getpass("again：")

        if (" " in name) or (" " in passwd):
            print("用户名密码不能有空格")
            continue
        if passwd != passwd1:
            print("两次密码不一致")
            continue
        msg = "R %s %s"%(name,passwd)
        s.send(msg.encode())
        #等待回复
        data = s.recv(128).decode()
        if data == 'ok':
            print("注册成功")
        elif data =='EXISTS':
            print("用户已存在")
        else:
            print("注册失败")
        return
def do_login(s):
    name = input("User:")
    passwd = getpass.getpass("password:")
    msg = "E %s %s"%(name,passwd)
    s.send(msg.encode())
    data = s.recv(128).decode()
    if data == 'ok':
        #进入第二界面
        print("进入第二界面")
        login(s,name)
    elif data == 'FAIL':
        print("此用户不存在")
    elif data == 'ERROR':
        print("密码错误")
    return

def login(s,name):
    print("用户名：",name)
    while True:
        print("========== Welcome ==========")
        print("***********1 查询 ***********")
        print("*********  2 历史记录 ********")
        print("***********3 注销 ***********")
        print("============================")
        cmd = input("请输入>>")
        if cmd not in ['1','2','3']:
            print("请输入正确的选项")
            sys.stdin.flush() #清除标准输入
            continue
        elif cmd == '1':
            do_find(s,name)
        elif cmd == '2':
            do_hist(s,name)
        elif cmd =='3':
            return

def do_find(s,name):
    while True:
        word = input("请输入要查询的单词：")
        msg = 'F '+word +' '+ name
        s.send(msg.encode())
        time.sleep(0.2)
        txt = s.recv(1024).decode()
        if txt == 'NONE':
            print("没有该单词")
            continue
        elif txt == "CLOSE":
            return
        print(txt)

def do_hist(s,name):
    msg = "H "+name
    s.send(msg.encode())
    while True:
        data = s.recv(1024).decode()
        if data == "##":
            break
        data = data.split(" ")
        time = " ".join(data[2:]).strip()
        print("姓名:%s 单词:%s 日期:%s"%(data[0],data[1],time))



main()