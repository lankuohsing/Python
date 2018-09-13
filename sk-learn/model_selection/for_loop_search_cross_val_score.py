# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 12:07:57 2018

@author: l00467141
"""

import numpy as np
from sklearn.datasets import load_iris
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
iris = load_iris()
X_trainval, X_test, y_trainval, y_test = train_test_split(iris.data, iris.target, random_state=0)   #总集——>训练验证集+测试集
X_train, X_valid, y_train, y_valid = train_test_split(X_trainval, y_trainval, random_state=1)   #训练验证集——>训练集+验证集
best_score = 0
for gamma in [0.001, 0.01, 0.1, 1, 10, 100]:
    for C in [0.001, 0.01, 0.1, 1, 10, 100]:
        svm = SVC(gamma=gamma, C=C)
        scores = cross_val_score(svm, X_trainval, y_trainval, cv=5)   #在训练集和验证集上进行交叉验证
        score = np.mean(scores)   # compute mean cross-validation accuracy
        if score > best_score:   
            best_score = score
            best_parameters = {'C': C, 'gamma': gamma}

# rebuild a model on the combined training and validation set
print('网格搜索for循环<有cross_val_score交叉验证>获得的最好参数组合:',best_parameters)
print(' ')
svmf = SVC(**best_parameters)
svmf.fit(X_trainval, y_trainval)
print('网格搜索<有交叉验证>获得的最好估计器,在训练验证集上没做交叉验证的得分:',svmf.score(X_trainval,y_trainval))#####
print(' ')
scores = cross_val_score(svmf, X_trainval, y_trainval, cv=5)   #在训练集和验证集上进行交叉验证   
print('网格搜索<有交叉验证>获得的最好估计器,在训练验证集上做交叉验证的平均得分:',np.mean(scores))   #交叉验证的平均accuracy   
print(' ')
print('网格搜索<有交叉验证>获得的最好估计器,在测试集上的得分:',svmf.score(X_test,y_test))#####
# print(' ')
# print(' ')
# scoreall = cross_val_score(svmf, iris.data, iris.target, cv=5)  
# print(scoreall ,np.mean(scoreall)) 
# In[]
"""
svm1=SVC()
svm1.fit(X_trainval, y_trainval)
print(svm1.score(X_test,y_test))
svmf = SVC(**best_parameters)
svmf.fit(X_trainval, y_trainval)
print(svmf.score(X_test,y_test))
"""