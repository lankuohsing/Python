# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 11:08:55 2018

@author: l00467141
"""
"""没指定数据切分方式，直接选用cross_val_score按默认切分方式进行交叉验证评估得分"""
# In[]
from sklearn.model_selection import cross_val_score
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
# In[]
iris = load_iris()
logreg = LogisticRegression()
# In[]
scores = cross_val_score(logreg, iris.data, iris.target, cv=5)
#默认cv=3,没指定默认在训练集和测试集上进行交叉验证
print(scores)

#Output:
#array([ 1.        ,  0.96666667,  0.93333333,  0.9       ,  1.        ])