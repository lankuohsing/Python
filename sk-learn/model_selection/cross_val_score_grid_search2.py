# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 15:51:58 2018

@author: l00467141
"""

# In[]
from sklearn.datasets import load_iris
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import cross_val_score
from sklearn.svm import SVC
# In[]
iris = load_iris()
param_grid = {'C': [0.001, 0.01, 0.1, 1, 10, 100],'gamma': [0.001, 0.01, 0.1, 1, 10, 100]}
svm_clf=GridSearchCV(SVC(), param_grid, cv=5)
print(svm_clf)
# In[]
scores = cross_val_score(svm_clf, iris.data, iris.target, cv=5)   
#选定网格搜索的每一组超参数,对训练集与测试集的交叉验证(cross_val_score没指定数据集合分割的默认情况)
print("Cross-validation scores: ", scores)
print("Mean cross-validation score: ", scores.mean())