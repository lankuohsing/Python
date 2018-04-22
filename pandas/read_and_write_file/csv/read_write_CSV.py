# -*- coding: utf-8 -*-
"""
Created on Sat Jun  3 10:33:55 2017

@author: lankuohsing
"""

import pandas as pd
import numpy as np
# In[]
path='D:/Projects/Github/Python/pandas/read_and_write_file/csv/iris.csv'
#header=0,index_col=0 第0行（列）作为列（行）标题
iris_df=pd.read_csv(path,header=0,index_col=0,encoding='utf-8')
iris_np=iris_df.iloc[:,0:4].as_matrix()
iris_label=np.reshape(iris_df.iloc[:,4].as_matrix(),(-1,1))
# In[]
path1='D:/Projects/Github/Python/pandas/read_and_write_file/csv/iris1.csv'
header=['sepal length in cm',	'sepal width in cm','petal length in cm',
        'petal width in cm','class label']
iris1_np=np.hstack((iris_np, iris_label))
iris1_df=pd.DataFrame(iris1_np)
iris1_df.to_csv(path1,sep=',',header=header,index_label =range(iris_np.shape[0]))
# In[]
#推荐这种方式   recommended
path2='D:/Projects/Github/Python/pandas/read_and_write_file/csv/iris2.csv'
iris2_df=pd.DataFrame(iris1_np,index=range(iris_np.shape[0]),columns=header)
iris2_df.to_csv(path2)