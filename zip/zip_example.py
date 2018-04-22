# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 17:44:58 2018

@author: lankuohsing
"""

# In[]
a = [1,2,3]
b = [4,5,6]
c = [4,5,6,7,8]
zipped_ab = zip(a,b)     # 打包为元组的列表
print(list(zipped_ab))
# In[]
zipped_ac=zip(a,c)              # 元素个数与最短的列表一致
print(list(zipped_ac))#注意，在打印时，不能和前面的zip操作分开，需要紧连着，否则list为空
# In[]
zipped_ab = zip(a,b)
d=zip(*zipped_ab)          # 与 zip 相反，可理解为解压，返回二维矩阵式
print(list(d))