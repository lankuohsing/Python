# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 00:54:27 2017

@author: lankuohsing
"""

import tensorflow as tf
import os
BASE_DIR = os.getcwd() #获取当前文件夹的绝对路径
v1 = tf.Variable(tf.random_normal([1,2]), name="v1")
v2 = tf.Variable(tf.random_normal([2,3]), name="v2")
saver = tf.train.Saver()

with tf.Session() as sess:
    saver.restore(sess, BASE_DIR+"/tmp3/model.meta")
    print ("Model restored")