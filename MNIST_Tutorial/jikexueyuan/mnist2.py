# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 00:05:15 2017
Deep MNIST for Experts
@author: lankuohsing
"""
#自动下载和导入MNIST数据集
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets('MNIST_data', one_hot=True)
#创建一个和C++后端的链接session
import tensorflow as tf
sess = tf.InteractiveSession()
#为输入图像和目标输出类别创建结点，开始构建计算图
x = tf.placeholder("float", shape=[None, 784])#占位符，行数为none（不确定），列数为784
y_ = tf.placeholder("float", shape=[None, 10])
#为模型定义权重W和偏置b
W = tf.Variable(tf.zeros([784,10]))
b = tf.Variable(tf.zeros([10]))
#为所有变量分配初始值
sess.run(tf.initialize_all_variables())
#类别预测函数
y = tf.nn.softmax(tf.matmul(x,W) + b)
#损失函数
cross_entropy = -tf.reduce_sum(y_*tf.log(y))
#采用最速下降法让交叉熵下降，步长为0.01
train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)
#执行1000次迭代
for i in range(1000):

    #每一步迭代，加载50个样本
    batch = mnist.train.next_batch(50)
    #执行train_step，将x和y_用训练数据代替
    train_step.run(feed_dict={x: batch[0], y_: batch[1]})
#将预测标签与实际标签对比
correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))
print(accuracy.eval(feed_dict={x: mnist.test.images, y_: mnist.test.labels}))
