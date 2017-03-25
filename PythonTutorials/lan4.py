# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 22:58:25 2017

@author: lankuohsing
"""

#Fibonacci series: 斐波那契数列
#两个元素的综合确定了下一个数
a, b = 0, 1
while b<10:
    print(b, end=' ')
    a,b=b,a+b