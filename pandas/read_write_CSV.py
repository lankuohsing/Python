# -*- coding: utf-8 -*-
"""
Created on Sat Jun  3 10:33:55 2017

@author: lankuohsing
"""

import pandas as pd
obj=pd.read_csv('./ceshi1.csv',header=0,encoding="gbk")
print(obj)
print(type(obj))
print(obj.dtypes)