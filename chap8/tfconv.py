# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 16:31:38 2019

@author: HAX
"""

import tensorflow as tf

input1=tf.Variable(tf.constant(1.0,shape=[1,5,5,1]))
input2=tf.Variable(tf.constant(1.0,shape=[1,5,5,2]))
input3=tf.Variable(tf.constant(1.0,shape=[1,4,4,1]))

filter1=tf.Variable(tf.constant([-1.0,0,0,-1],shape=[2,2,1,1]))
filter2=tf.Variable(tf.constant([-1.0,0,0,-1,
                                 -1.0,0,0,-1],shape=[2,2,1,2]))
filter3=tf.Variable(tf.constant([-1.0,0,0,-1,-1.0,0,0,-1,-1.0,0,0,-1],shape=[2,2,1,3]))
filter4=tf.Variable(tf.constant([-1.0,0,0,-1,
                                 -1.0,0,0,-1,
                                 -1.0,0,0,-1,
                                 -1.0,0,0,-1],shape=[2,2,2,2]))
filter5=tf.Variable(tf.constant([-1.0,0,0,-1,-1.0,0,0,-1],shape=[2,2,2,1]))

op1=tf.nn.conv2d(input1,filter1,strides=[1,2,2,1],padding='SAME')
op2=tf.nn.conv2d(input1,filter2,strides=[1,2,2,1],padding='SAME')
op3=tf.nn.conv2d(input3,filter3,strides=[1,2,2,1],padding='SAME')
op4=tf.nn.conv2d(input2,filter4,strides=[1,2,2,1],padding='SAME')
op5=tf.nn.conv2d(input2,filter5,strides=[1,2,2,1],padding='SAME')
vop1=tf.nn.conv2d(input1,filter1,strides=[1,2,2,1],padding='VALID')
op6=tf.nn.conv2d(input3,filter1,strides=[1,2,2,1],padding='SAME')
vop6=tf.nn.conv2d(input3,filter1,strides=[1,2,2,1],padding='VALID')

with tf.Session()  as sess:
    sess.run(tf.global_variables_initializer())
    print('op1:\n',sess.run([op1,filter1]))
    print('--------------')
    print('op2:\n',sess.run([op2,filter2]))
    print('op3\n',sess.run([op3,filter3]))
    print('--------------')
    print('op4\n',sess.run([op4,filter4]))
    print('op5\n',sess.run([op5,filter5]))
    print('---------------')
    print('op1\n',sess.run([op1,filter1]))
    print('vpo1\n',sess.run([vop1,filter1]))
    print('op6\n',sess.run([vop6,filter1]))