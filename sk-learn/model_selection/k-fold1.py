# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 11:22:41 2018

@author: l00467141
"""

# In[]
from sklearn.model_selection import cross_val_score
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import KFold
# In[]
iris = load_iris()
logreg = LogisticRegression()
kfold = KFold(n_splits=5, shuffle=True, random_state=0)
#shuffle添加了随机扰动,打乱样本顺序,再进行k折切分样本
# In[]
scores =cross_val_score(logreg, iris.data, iris.target, cv=kfold)
print(scores)