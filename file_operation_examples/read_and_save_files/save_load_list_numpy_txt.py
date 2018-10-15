# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 21:42:55 2018

@author: l00467141
"""

# In[]
import numpy as np
# In[]
numpy_data=np.array([[1,2,3],[4,5,6]])

np.savetxt("numpy_data.txt", numpy_data)

numpy_data1=np.loadtxt("numpy_data.txt")
# In[]
list_data=[1,2,3,4,5]
file=open('list_data.txt','w') 
file.write(str(list_data)); 
file.close() 