from test import *
from multiprocessing import Process 
import time 

def io():
    write()
    read()

jobs = []
t = time.time()
for i in range(10):
    th = Process(target=io)
    jobs.append(th)
    th.start()
for i in jobs:
    i.join()
print("Thread cpu",time.time()-t)