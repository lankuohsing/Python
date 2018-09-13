# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 15:09:43 2018

@author: l00467141
"""
# In[]
import numpy as np
from sklearn.datasets import load_iris
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score

iris = load_iris()


param_grid = {'C': [0.001, 0.01, 0.1, 1, 10, 100],'gamma': [0.001, 0.01, 0.1, 1, 10, 100]}
X_trainvalid, X_test, y_trainvalid, y_test = train_test_split(iris.data, iris.target, random_state=0)   #default=0.25
grid_search = GridSearchCV(SVC(), param_grid, cv=5)   #网格搜索+交叉验证
grid_search.fit(X_trainvalid, y_trainvalid)
print('GridSearchCV交叉验证网格搜索字典获得的最好参数组合',grid_search.best_params_)
print(' ')
print('GridSearchCV交叉验证网格搜索获得的最好估计器,在训练验证集上没做交叉验证的得分',grid_search.score(X_trainvalid,y_trainvalid))#####
print(' ')
print('GridSearchCV交叉验证网格搜索获得的最好估计器,在**集上做交叉验证的平均得分',grid_search.best_score_)#?????   
# print(' ')
# print('BEST_ESTIMATOR:',grid_search.best_estimator_)   #对应分数最高的估计器
print(' ')
print('GridSearchCV交叉验证网格搜索获得的最好估计器,在测试集上的得分',grid_search.score(X_test, y_test))#####