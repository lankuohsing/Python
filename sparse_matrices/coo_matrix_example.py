# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 19:50:01 2018

@author: lankuohsing
"""
#coo_matrix无法进行常用的矩阵操作，除非将其转换为其他稀疏矩阵格式
# In[]
from scipy.sparse import coo_matrix
import numpy as np
# In[]
a=coo_matrix((3, 4), dtype=np.int8)
b=a.toarray()

# In[]
row  = np.array([0, 3, 1, 0])
col  = np.array([0, 3, 1, 2])
data = np.array([4, 5, 7, 9])
a=coo_matrix((data, (row, col)), shape=(4, 4))
b=a.toarray()
# In[]
c=scipy.sparse.lil_matrix(a)