from multiprocessing import Array,Process 
import time

#创建共享内存
# shm = Array('1',[1,2,3,4])

#开辟五个ｉｎｔ空间
# shm = Array('i',5)

#存入字符串
shm = Array('c',b'hello')

def fun():
    for i in shm:
        print(i)
    # shm[0] = 1000 #修改共享内存
    shm[0] = b'H'
p = Process(target=fun)
p.start()
p.join()

for i in shm:
    print(i)

print(shm.value)　#打印字符串