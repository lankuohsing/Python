# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 16:09:35 2017

@author: lankuohsing
"""
#==============================================================================
# TensorFlow官方教程之利用softmax回归对MNIST数据集进行分类
#==============================================================================
#导入数据
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
#导入TensorFlow
import tensorflow as tf
#x代表图片，W代表模型中x的系数，b代表模型中的截距b
x = tf.placeholder(tf.float32, [None, 784])
W = tf.Variable(tf.zeros([784,10]))
b = tf.Variable(tf.zeros([10]))

#计算softmax模型
#注：一个矩阵加上一个行向量，等效于矩阵的每行都加那个行向量
y = tf.nn.softmax(tf.matmul(x,W) + b)
y_ = tf.placeholder(tf.float32, [None,10])
#cross_entropy = -tf.reduce_sum(y_*tf.log(y))
#计算交叉熵
#注意，这里的*，是两个矩阵的每个对应的元素相乘，所以相乘的两个矩阵必须维数一模一样
cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y), reduction_indices=[1]))
#使用反向传播算法，调用梯度下降算法最小化交叉熵
train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)
#初始化所有变量
init = tf.initialize_all_variables()
sess = tf.Session()
sess.run(init)
for i in range(1000):
  batch_xs, batch_ys = mnist.train.next_batch(100)
  sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})

correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))
print(sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels}))
# 任务完成, 关闭会话.
sess.close()