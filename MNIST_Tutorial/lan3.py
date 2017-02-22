# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 22:05:19 2017

@author: lankuohsing
"""

import tensorflow as tf
sess = tf.InteractiveSession()
x=tf.constant([[1],[2],[3]])
y=tf.constant([[1],[2],[1]])
z = tf.equal(x, y)

accuracy = tf.reduce_mean(tf.cast(z, "float"))
print(sess.run(accuracy))
sess.close()