# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 01:11:22 2018

@author: l00467141
"""
# In[]
import numpy as np
# In[]
class OneHotEncoder(object):
    def __init__(
            self
            ):
        self.row=None
        self.cols=None
        # In[]
        self.ori_list_list=[]
        self.ori_set_list=[]
        self.feature_list_list=[]
        
    def fit(
            self,
            X_ori
            ):
        self.rows,self.cols=X_ori.shape
        for i in range(self.cols):
            self.ori_list_list.append(list(X_ori[:,i]))
            self.ori_set_list.append(set(self.ori_list_list[i]))
            self.feature_list_list.append(list(self.ori_set_list[i]))
            
    def transform(
            self,
            Y_ori
            ):
        # In[]
        one_hot_feature_list=[]
        one_hot_cols_list=[]
        for i in range(self.cols):
            cols_i=len(self.feature_list_list[i])
            np_i=np.zeros((self.rows,cols_i))
            for j in range(self.rows):
                if(Y_ori[j,i] in self.feature_list_list[i]):
                    np_i[j,self.feature_list_list[i].index(Y_ori[j,i])]=1
            one_hot_feature_list.append(np_i)   
        # In[]
        one_hot_feature=one_hot_feature_list[0]   
        for i in range(1,len(one_hot_feature_list)):
            one_hot_feature=np.hstack((one_hot_feature,one_hot_feature_list[i])) 
        return one_hot_feature
    def fit_transform(
            self,
            X_ori
            ):
        self.fit(X_ori)
        return self.transform(X_ori)
     
# In[]
if __name__=="__main__":

    X_ori =np.array([['Male', 1], ['Female', 3,], ['Female', 2]])
    Y_ori =np.array([['Male', 4], ['a', 3,], ['Female', 2]])
    a=OneHotEncoder()
    c=a.fit_transform(X_ori)
    b=a.transform(Y_ori)