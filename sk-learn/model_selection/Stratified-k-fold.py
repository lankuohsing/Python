# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 16:41:18 2018

@author: l00467141
"""

# In[]
import numpy as np 
from sklearn.model_selection import KFold,StratifiedKFold
# In[]
X=np.array([
    [1,2,3,4],
    [11,12,13,14],
    [21,22,23,24],
    [31,32,33,34],
    [41,42,43,44],
    [51,52,53,54],
    [61,62,63,64],
    [71,72,73,74]
])

y=np.array([1,1,0,0,1,1,0,0])
#n_folds这个参数没有，引入的包不同，
floder = KFold(n_splits=4,random_state=0,shuffle=True)
sfolder = StratifiedKFold(n_splits=4,random_state=0,shuffle=True)
# In[]
print("Skfold:")
for train, test in sfolder.split(X,y):
    print('Train: %s | test: %s' % (train, test))
    print(" ")
print("kfold:")
for train, test in floder.split(X,y):
    print('Train: %s | test: %s' % (train, test))
    print(" ")