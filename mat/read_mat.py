# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 19:35:34 2018

@author: lankuohsing
"""
import scipy.io as sio
import numpy as np
# In[]
###下面是讲解python怎么读取.mat文件以及怎么处理得到的结果###
load_fn = 'save2.mat'
load_data = sio.loadmat(load_fn)
load_matrix = load_data['array_x'] #假设文件中存有字符变量是matrix，例如matlab中save(load_fn, 'matrix');当然可以保存多个save(load_fn, 'matrix_x', 'matrix_y', ...);
load_matrix_row = load_matrix[0] #取了当时matlab中matrix的第一行，python中数组行排列