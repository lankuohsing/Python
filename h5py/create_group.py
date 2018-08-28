# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 15:39:50 2018

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
f=h5py.File("group_exam.hdf5","w")

#创建一个名字为bar的组
g1=f.create_group("bar1")

#在bar这个组里面分别创建name为dset1,dset2的数据集并赋值。
g1["dset1"]=np.arange(10)
g1["dset2"]=np.arange(12).reshape((3,4))
g2=f.create_group("bar2")

#在bar这个组里面分别创建name为dset1,dset2的数据集并赋值。
g2["dset1"]=np.arange(20)
g2["dset2"]=np.arange(32).reshape((8,4))
for key in g1.keys():
    print(g1[key].name)
    print(g1[key].value)
for key in g2.keys():
    print(g2[key].name)
    print(g2[key].value)
# In[]
f.close()