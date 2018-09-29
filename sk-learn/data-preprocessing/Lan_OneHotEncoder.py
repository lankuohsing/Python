# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 01:11:22 2018

@author: l00467141
"""
# In[]
import numpy as np
# In[]
class OneHotEncoder(object):
    """
    feature_list_list：存了每列特征的原始向量，列表的每个元素是一个列表，
                       列表中是对应特征的所有取值（不重复）
    """
    def __init__(
            self
            ):
        self.row=None
        self.cols=None
        # In[]
        self.ori_np_list=[]
        self.ori_set_list=[]
        self.feature_list_list=[]
        
    def fit(
            self,
            X_ori
            ):
        self.rows,self.cols=X_ori.shape
        for i in range(self.cols):
            self.ori_np_list.append(list(X_ori[:,i]))
            self.ori_set_list.append(set(self.ori_np_list[i]))
            self.feature_list_list.append(list(self.ori_set_list[i]))
            
    def transform(
            self,
            Y_ori
            ):
        # In[]
        one_hot_feature_list=[]
        Y_rows,Y_cols=Y_ori.shape
        for i in range(self.cols):
            np_i=np.zeros((Y_rows,len(self.feature_list_list[i])))
            for j in range(Y_rows):
                if(Y_ori[j,i] in self.feature_list_list[i]):
                    np_i[j,self.feature_list_list[i].index(Y_ori[j,i])]=1
            one_hot_feature_list.append(np_i)   
        # In[]
        one_hot_feature_np=one_hot_feature_list[0]   
        for i in range(1,len(one_hot_feature_list)):
            one_hot_feature_np=np.hstack((one_hot_feature_np,one_hot_feature_list[i])) 
        return one_hot_feature_np
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
    Z_ori =np.array([['Male', 4]])
    a=OneHotEncoder()
    c=a.fit_transform(X_ori)
    b=a.transform(Y_ori)
    d=a.transform(Z_ori)