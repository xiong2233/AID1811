from select import select
from socket import *
s = socket()
s.bind(('0.0.0.0',8888))
s.listen(5)
print("监听ＩＯ")
rs,ws,xs = select([s],[],[],10)
print("就绪rs",rs)
print("就绪ws",ws)
print("就绪xs",xs)