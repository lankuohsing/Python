# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 22:57:14 2017

@author: lankuohsing
"""
import tensorflow as tf
# Create some variables.
weights = tf.Variable(tf.random_normal([784, 200], stddev=0.35),
                      name="weights")
biases = tf.Variable(tf.zeros([200]), name="biases")

# Add ops to save and restore all the variables.
saver = tf.train.Saver()

# Later, launch the model, use the saver to restore variables from disk, and
# do some work with the model.
with tf.Session() as sess:
  # Restore variables from disk.
  saver.restore(sess, "/tmp2/model.ckpt")
  print ("Model restored.")
  # Do some work with the model
  #print(v1)