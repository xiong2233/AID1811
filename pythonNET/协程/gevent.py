import gevent
from time import sleep
def foo(a,b):
    print("Running foo",a,b)
    gevent.sleep(2)
    pritn("Running foo again")
def bar():
    print("Running bar")
    gevent.sleep(3)
    pritn("Running bar again")
#创建协程对象
f = gevent.spawn(foo,1,2)
b = gevent.spawn(bar)
#回收协程
gevent.joinall()