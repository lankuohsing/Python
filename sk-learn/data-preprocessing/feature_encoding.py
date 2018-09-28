# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 19:58:56 2018

@author: lankuohsing
"""

# In[]sklearn 
measurements = [
    {'city': 'Dubai', 'temperature': 33.,'gender':'女'},
    {'city': 'London', 'temperature': 12.,'gender':'男'},
    {'city': 'San Fransisco', 'temperature': 18.,'gender':'男'},
    {'city': 'San Fransisco', 'temperature': 18.,'gender':'男'},
]
#list
measurements1 = [
    {'city': 'London', 'temperature': 10.,'gender':'女'},
    {'city': 'Shanghai', 'temperature': 1.,'gender':'女'},
    {'city': 'San Fransisco', 'temperature': 1.,'gender':'男'},
    {'city': 'San Fransisco', 'temperature': 1.,'gender':'男'},
]
from sklearn.feature_extraction import DictVectorizer
vec = DictVectorizer()
trans_vec = vec.fit_transform(measurements).toarray();
print(trans_vec)
print(vec.transform(measurements1).toarray());#Shanghai在之前没出现过，因此为全零向量
print(vec.get_feature_names())


# In[]
"""LabelEncoder"""
#简单来说 LabelEncoder 是对不连续的数字或者文本进行编号
from sklearn import preprocessing
le = preprocessing.LabelEncoder()
le.fit([1, 2, 2, 6])
#LabelEncoder()
print(le.classes_)
#array([1, 2, 6])
print(le.transform([1, 1, 2, 6]) )
#array([0, 0, 1, 2]...)
print(le.inverse_transform([0, 0, 1, 2]))
#array([1, 1, 2, 6])
# In[]
le = preprocessing.LabelEncoder()
le.fit(["paris", "paris", "tokyo", "amsterdam"])
#LabelEncoder()
print(list(le.classes_))
#['amsterdam', 'paris', 'tokyo']
print(le.transform(["tokyo", "tokyo", "paris"]) )
#array([2, 2, 1]...)
print(list(le.inverse_transform([2, 2, 1])))
#['tokyo', 'tokyo', 'paris']

# In[]
"""OneHotEncoder"""
from sklearn.preprocessing import OneHotEncoder
enc = OneHotEncoder(handle_unknown='ignore')
print(enc.fit([[0, 0, 3], [1, 1, 0], [0, 2, 1], [1, 0, 2]]))
print(enc.n_values_)#每个特征对应的最大位数
print(enc.transform([[0,1,4]]).toarray())
print(enc.transform([[0,1,1]]).toarray())
