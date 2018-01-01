# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 14:26:04 2018

@author: lankuohsing
"""

# In[]
"""
目的是将自定义的模块的路径加入到python的搜索路径目录中
"""
import sys
import os
print(os.getcwd())
path='D:\Projects\Github\Python\self_define_functions'
sys.path.append(path)
# In[]
from sse_within_cluster import *
import numpy as np
# In[]
points=np.array([[1,2],[3,4],[5,6]])
print(get_SSE(points))
