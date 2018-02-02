# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 14:16:32 2018
将多个list合并为一个list的例子
@author: lankuohsing
"""

# In[]
list1=[1,2,3]
list2=['a','b']
list3=[4,5,6,7]
# In[]
"""
使用'+'号完成操作
"""
list4=list1+list2
print(list4)

# In[]
"""
使用extend方法
"""
list3.extend(list1)
print(list3)
# In[]
"""
使用切片。注：可扩展为将一个列表插入另一个列表的任意位置
"""
list3[len(list3):len(list3)]=list2
print(list3)