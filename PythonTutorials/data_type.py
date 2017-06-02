# -*- coding: utf-8 -*-
"""
Created on Thu May 11 22:05:35 2017

@author: lankuohsing
"""
'''
a = 1       # 整数
b = 1.2     # 浮点数
c = True    # 布尔类型
d = "False" # 字符串
e = None    # NoneType
print(a)
print(b)
print(c)
print(d)
print(e)

type(a)     # <type 'int'>
type(b)     # <type 'float'>
type(c)     # <type 'bool'>
type(d)     # <type 'str'>
type(e)     # <type 'NoneType'>，None是单独的一种类型，在很多API中，如果执行失败就会返回None

#Python中基本变量的赋值一般建立的是个引用
a = 1
b = a
c = 1
#a赋值为1后，b=a执行时并不会将a的值复制一遍，然后赋给b，而是简单地为a所指的值，
#也就是1建立了一个引用，相当于a和b都是指向包含1这个值的这块内存的指针。
#所以c=1执行的也是个引用建立，这三个变量其实是三个引用，指向同一个值。
id(a)   # 35556792L
id(b)   # 35556792L
id(c)   # 35556792L
'''
#字符串前加r表示字符串内容严格按照输入的样子，好处是不用转义符了，非常方便。
e = '\n\t\\'   
print(e)        # '\\n\\t\\\\'
e = r'\n\t\\'   
print(e)        # '\\n\\t\\\\'
