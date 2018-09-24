# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 19:58:56 2018

@author: lankuohsing
"""

# In[]
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

