# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 08:57:38 2019

@author: HAX
"""

import numpy as np
import tensorflow as tf
c=tf.constant(0.0)
g=tf.Graph()
with g.as_default():
    c1=tf.constant(0.0)
    print(c1.graph)
    print(g)
    print(c.graph)
g2=tf.get_default_graph()
print(g2)
tf.reset_default_graph()
g3=tf.get_default_graph()
print(g3)

print(c1.name)
t=g.get_tensor_by_name(name='Const:0')
print(t)
    
a=tf.constant([[1.0,2.0]])
b=tf.constant([[1.0],[3.0]])
tensor1=tf.matmul(a,b,name='exampleop')
print(tensor1.name,tensor1)
test=g3.get_tensor_by_name('exampleop:0')
print(test)

print(tensor1.op.name)
testop=g3.get_operation_by_name('exampleop')
print(testop)

with tf.Session() as sess:
    test=sess.run(test)
    print(test)
    test=tf.get_default_graph().get_tensor_by_name('exampleop:0')
    print(test)