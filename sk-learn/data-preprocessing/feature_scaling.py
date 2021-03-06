# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 20:25:21 2018

@author: lankuohsing
"""
import numpy as np
from sklearn.preprocessing import MinMaxScaler
# In[]
data = np.array([[-1, 2], [-0.5, 6], [0, 10], [1, 18]])#数据样例
data2=10*np.array([[-1, 2], [-0.5, 6], [0, 10], [1, 18]])#数据样例
feature_range=(0,1)#归一化的范围,类型为tuple
# In[]
"""
X_std = (X - X.min(axis=0)) / (X.max(axis=0) - X.min(axis=0))
X_scaled = X_std * (max - min) + min
"""
scaler = MinMaxScaler(copy=True,feature_range=feature_range)#copy=True保留原始数据矩阵
scaled_data=scaler.fit_transform(data)
data_orign=(scaled_data-feature_range[0])/(feature_range[1]-feature_range[0])\
*(scaler.data_max_-scaler.data_min_)+scaler.data_min_#恢复成原来的数据
# In[]
print(scaler.data_min_)
print(scaler.data_max_)
print(scaled_data)
#print(scaler.data_range_)
# In[]
#print(feature_range[0])
# In[]
scaled_data=(data-scaler.data_min_)/(scaler.data_max_-scaler.data_min_)
print(scaled_data)
# In[]
scaled_data2=(data2-scaler.data_min_)/(scaler.data_max_-scaler.data_min_)
print(scaled_data2)
# In[]
scaled_data3=scaler.transform(data2)

print(scaled_data3)