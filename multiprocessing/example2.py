# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 00:34:23 2018

@author: lankuohsing
"""
# In[]
import time
def task(i):
    return i*i
result1=[]
start = time.time()
for i in range(1000000):
    a=0
    a=i*i*i
    result1.append(a)
end = time.time()
print('串行所用时间：%d 秒'%(end-start))
# In[]
from multiprocessing import Pool
import time
def task():
    time.sleep(1)

start = time.time()
pool = Pool()
for i in range(50):
    pool.apply_async(task)
end = time.time()
print('并行所用时间：%d 秒'%(end-start))
pool.close()
#pool.join()