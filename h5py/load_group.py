# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 15:44:51 2018

@author: lankuohsing
"""

# In[]
import h5py
import numpy as np
import os,sys
path = 'D:\Projects\Github\Python\h5py'
#修改当前工作目录
os.chdir(path)
# In[]
# Load hdf5 dataset
f = h5py.File('group_exam.hdf5', 'r')
# In[]
print([key for key in f.keys()])#python2 返回为list，python3 返回为view-like objects，不能直接查看
# In[]
for key in f.keys():
    print(f[key].name)
    for key1 in f[key].keys():
        print(f[key][key1].name)
        print(f[key][key1].value)
# In[]
f.close()