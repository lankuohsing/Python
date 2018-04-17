# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 19:23:56 2018

@author: lankuohsing
"""

import scipy.io as sio
import numpy as np

# In[]

###下面是讲解python怎么保存.mat文件供matlab程序使用###
save_fn1 = 'save1.mat'
save_array = np.array([1,2,3,4])
sio.savemat(save_fn1, {'array': save_array}) #和上面的一样，存在了array变量的第一行
# In[]
save_fn2 = 'save2.mat'
save_array_x = np.array([1,2,3,4])
save_array_y = np.array([5,6,7,8])
sio.savemat(save_fn2, {'array_x': save_array_x, 'array_y': save_array_y}) #同理，只是存入了两个不同的变量供使用
