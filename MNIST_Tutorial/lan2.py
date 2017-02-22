# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 21:10:31 2017

@author: lankuohsing
"""

import tensorflow as tf
sess = tf.InteractiveSession()

x=tf.constant([[1,2,3],[4,5,6]])
x1=tf.reduce_sum(x)
print(x1.eval())
#==============================================================================
# tf.reduce_sum(x, 0) ==> [2, 2, 2]
# tf.reduce_sum(x, 1) ==> [3, 3]
# tf.reduce_sum(x, 1, keep_dims=True) ==> [[3], [3]]
# tf.reduce_sum(x, [0, 1]) ==> 6
#==============================================================================
