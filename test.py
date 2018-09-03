# -*- coding:utf-8 -*-
"""
@contact: adonis_wu@outlook.com
@file: test.py
@time: 2018/8/30 10:01
"""
__author__ = '🍊 Adonis Wu 🍊'

import tensorflow as tf

a = tf.ones(shape=(5,6))

c = a.get_shape().with_rank(2)[1]
d = tf.unstack(a, axis=0)
e = tf.unstack(a, axis=1)


with tf.Session() as sess:
    print(sess.run(c))
