# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 21:50:55 2019

@author: lankuohsing
"""
'''
https://scikit-learn.org/stable/modules/decomposition.html#lsa
'''
# In[]
from sklearn.datasets import load_iris
from sklearn.decomposition import TruncatedSVD
import matplotlib.pyplot as plt
import numpy as np
# In[]
iris = load_iris()
iris_data = iris.data
# In[]
svd = TruncatedSVD(2)
iris_transformed = svd.fit_transform(iris_data)
# In[]
print(iris_data[:5])

print(iris_transformed[:5])


# In[]

f = plt.figure(figsize=(5, 5))
ax = f.add_subplot(111)

ax.scatter(iris_transformed[:, 0], iris_transformed[:, 1], c=iris.target)
ax.set_title("Truncated SVD, 2 Components")
# In[]
V=svd.components_#变换矩阵
X1=np.dot(iris_data,V.T)#这样得到的结果和iris_transformed是一样的
# In[]
X=svd.inverse_transform(X1)
a=iris_data-X
# In[]
print(float('inf')-1)