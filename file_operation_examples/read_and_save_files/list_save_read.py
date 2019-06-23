# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 15:35:43 2019

@author: lankuohsing
"""

# In[]
a=['a','b','c']
f=open('list1.txt','w',encoding="UTF-8")
f.writelines(str(a)+"\n")
f.close()
# In[]
f=open('list1.txt','r',encoding="UTF-8")
lines=f.readlines()
f.close()
# In[]
b=eval(lines[0])
# In[]
c=str(a)
# In[]
d=eval(c)