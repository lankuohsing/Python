# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 00:52:47 2017

@author: lankuohsing
"""

import tensorflow as tf
import os
BASE_DIR = os.getcwd() #获取当前文件夹的绝对路径
v1 = tf.Variable(tf.random_normal([1,2]), name="v1")
v2 = tf.Variable(tf.random_normal([2,3]), name="v2")
init_op = tf.initialize_all_variables()
saver = tf.train.Saver()
with tf.Session() as sess:
    sess.run(init_op)
    saver_path = saver.save(sess, BASE_DIR+"/tmp3/model")
    print ("Model saved in file: ", saver_path)