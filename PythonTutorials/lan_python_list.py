# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 23:19:27 2017

@author: lankuohsing
"""

classmates = ['languoxing', 'xujuanting', 'janet']
print(classmates)
print('classmates中的元素个数为：%d'% len(classmates))
classmates.append('lankuohsing')
print(classmates)
classmates.insert(1,'Garrison')
print(classmates)
classmates.pop()
print(classmates)
classmates.pop(1)
print(classmates)
classmates[1]='guoxinglan'
print(classmates)

L=['Apple',123,True]
print(L)
s=['python',classmates,L]
print(s)
classmates=('Michael', 'Bob', 'Tracy')
print(classmates)
t=(1,)#注意在1个元素的情况下，如果t是元组tuple，1后面必须有，
print(t)
t=('a', 'b', ['A', 'B'])
t[2][0]='X'
t[2][1]='Y'
print(t)