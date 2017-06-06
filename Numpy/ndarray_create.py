# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 17:43:40 2017

@author: lankuohsing
"""
import numpy as np
#通过array()函数传递Python的序列对象来创建数组
a=np.array([1,2,3,4])
b=np.array((5,6,7,8))
c=np.array([[1,2,3,4],[4,5,6,7],[7,8,9,10]])

print(a,a.shape)
print(b,b.shape)
print(c,c.shape)

c.shape=4,3#注意，并不会转置
print(c)

c.shape=2,-1#默认为2,6
print(c)

d=a.reshape((2,2))#也可以用a.reshape(2,2)
print(d)

a[1]=100
print(a)
print(d)

print(c.dtype)

v1=3.14
v2=np.float64(v1)
