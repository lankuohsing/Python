# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 11:08:42 2018

@author: l00467141
"""

# In[]
import numpy as np
from sklearn.datasets import dump_svmlight_file
from sklearn.datasets import load_svmlight_file
# In[]
X1=np.array([[1,0,0,2],[0,1,0,1],[0,0,1,2]])
y1=np.array([[1],[2],[3]]).flatten()
# In[]
dump_svmlight_file(X1,y1,"data1.txt")
# In[]
X2,y2=load_svmlight_file("data1.txt")