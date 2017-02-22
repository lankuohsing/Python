# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 20:03:24 2017

@author: lankuohsing
"""
#矩阵的一些操作
import tensorflow as tf
sess = tf.InteractiveSession()

# 2-D tensor `a`
a = tf.constant([[1,2],[4,3],[5,6]]) 
# 2-D tensor `b`
b = tf.constant([[5,6],[7,8],[9,10]]) 
c = tf.reduce_sum(a*b)
print(c.eval())
#==============================================================================
# W = tf.Variable(tf.zeros([5]))
# W.initializer.run()
# print(W.eval())
#==============================================================================
#==============================================================================
# sub = tf.sub(x, a)
# print(sub.eval())
#==============================================================================

# ==> [-2. -1.]