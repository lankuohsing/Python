# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 15:58:04 2018

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
X= np.random.rand(1,1000).astype('float32')
y = X*2+1
# In[]
# Create a new file
f = h5py.File('data.h5', 'w')
f.create_dataset('X_train', data=X)
f.create_dataset('y_train', data=y)
f.close()
# In[]
# Load hdf5 dataset
f = h5py.File('data.h5', 'r')
X = f['X_train'].value
Y = f['y_train'].value
f.close()