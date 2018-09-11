# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 23:43:17 2018

@author: lankuohsing
"""

from joblib import Parallel, delayed
import multiprocessing as multiprocessing
import time as time
# In[]
# what are your inputs, and what operation do you want to
# perform on each input. For example...
inputs = range(100000)
def processInput(i):
    return i * i
# In[]
time_start=time.time()
num_cores = multiprocessing.cpu_count()

results = Parallel(n_jobs=num_cores)(delayed(processInput)(i) for i in inputs)
time_end=time.time()
print("parallel:"%(time_end-time_start))
# In[]
results2=[]
time_start=time.time()
for i in inputs:
    results2.append(processInput(i))

time_end=time.time()
print("not parallel:",(time_end-time_start))