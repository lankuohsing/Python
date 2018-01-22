# -*- coding: utf-8 -*-
"""
Created on Sat Jun  3 10:33:55 2017

@author: lankuohsing
"""

import pandas as pd
import numpy as np
# In[]
obj=pd.read_csv('D:/Projects/Github/Python/pandas/read_and_write_file/csv/ceshi1.csv',header=0,encoding="gbk")
print(obj)
print(type(obj))
print(obj.dtypes)
# In[]
matrix=np.array([[1,2,3],[4,5,6],[7,8,9]])
np.savetxt('D:/Projects/Github/Python/pandas/read_and_write_file/csv/matrix.csv', matrix, delimiter = ',')