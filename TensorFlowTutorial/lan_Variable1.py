# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 22:50:02 2017

@author: lankuohsing
"""
import tensorflow as tf
# Create two variables.
weights = tf.Variable(tf.random_normal([784, 200], stddev=0.35),
                      name="weights")
biases = tf.Variable(tf.zeros([200]), name="biases")
...
# Add an op to initialize the variables.
init_op = tf.global_variables_initializer()

# Add ops to save and restore all the variables.
saver = tf.train.Saver()

# Later, launch the model, initialize the variables, do some work, save the
# variables to disk.
with tf.Session() as sess:
  sess.run(init_op)
  # Do some work with the model.
  
  # Save the variables to disk.
  save_path = saver.save(sess, "D:/Projects/Github/Python/TensorFlowTutorial/tmp2/model.ckpt")
  print ("Model saved in file: ", save_path)
  #print(weights)