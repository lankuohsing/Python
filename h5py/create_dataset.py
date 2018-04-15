# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 14:54:30 2018

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
f=h5py.File("myh5py.h5","w")#后缀名是啥都无所谓
# In[]
#创建方式1
#dset1是数据集的name，（20,）代表数据集的shape，i代表的是数据集的元素类型
d1=f.create_dataset("dset1", (20,), 'i')#此时未赋值
d1[...]=np.arange(20)#赋值方式1
#创建方式2
f["dset2"]=np.arange(15)#赋值方式2
#创建方式3
a=np.arange(10)
d3=f.create_dataset("dset3",data=a)#赋值方法3
for key in f.keys():
    print(key)
    print(f[key].dtype)
    b=f[key]
    print(f[key].name)
    print(f[key].shape)
    print(f[key].value)

# In[]
f.close()#close后无法对f进行操作，如果上次的f未关闭必须关闭才能重新打开
