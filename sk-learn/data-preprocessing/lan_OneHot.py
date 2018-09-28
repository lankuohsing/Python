# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 00:04:02 2018

@author: l00467141
"""

# In[]
import numpy as np
# In[]
X_ori =np.array([['Male', 1], ['Female', 3,], ['Female', 2]])

rows,cols=X_ori.shape
# In[]
ori_list_list=[]
ori_set_list=[]
feature_list_list=[]
for i in range(cols):
    ori_list_list.append(list(X_ori[:,i]))
    ori_set_list.append(set(ori_list_list[i]))
    feature_list_list.append(list(ori_set_list[i]))
# In[]
one_hot_feature_list=[]
one_hot_cols_list=[]
for i in range(cols):
    cols_i=len(feature_list_list[i])
    np_i=np.zeros((rows,cols_i))
    for j in range(rows):
        if(X_ori[j,i] in feature_list_list[i]):
            np_i[j,feature_list_list[i].index(X_ori[j,i])]=1
    one_hot_feature_list.append(np_i)   
# In[]
one_hot_feature=one_hot_feature_list[0]   
for i in range(1,len(one_hot_feature_list)):
    one_hot_feature=np.hstack((one_hot_feature,one_hot_feature_list[i])) 
# In[]

