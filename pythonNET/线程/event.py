from threading import Event 

#创建事件对象
e =　Event()
e.set() #设置ｅ
e.clear()　#
print(e.is_set())
p.wait()
e.wait()

print("******************")
