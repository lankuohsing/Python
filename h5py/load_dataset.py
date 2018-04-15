# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 15:30:21 2018

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
f = h5py.File('myh5py.h5', 'r')
X1 = f['dset1'].value
X2 = f['dset2'].value
X3=f['dset3'].value
f.close()