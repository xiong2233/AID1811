from multiprocessing import Process 
from time import sleep

#带参数的进程函数
def worker(sec,name):
    for i in range(3):
        sleep(sec)
        print("i'm %s"%name)
        print("i'am working...")

#按照位置传递参数
# p = Process(target = worker,args=(2,'Levi'))

#按照键的名称传递参数
p = Process(target = worker,kwargs={'sec':2,'name':'Levi'})
p.start()
p.join()