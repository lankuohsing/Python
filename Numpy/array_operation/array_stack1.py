# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 20:47:15 2018

@author: lankuohsing
"""
# In[]
import numpy as np
# In[]
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
b=np.array([[10,20,30],[40,50,60],[70,80,90]])
# In[]
#水平拼接
c=np.hstack((a,b))
#垂直拼接
d=np.vstack((a,b))

# In[]
a=np.array([[[1,2],[3,4],[5,6]],
            [[7,8],[9,10],[11,12]],
            [[13,14],[15,16],[17,18]],
            [[19,20],[21,22],[23,24]]])
b=-1*a
c=np.vstack((a,b))
d=np.hstack((a,b))