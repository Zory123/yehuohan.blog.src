
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import tensorflow as tf
from sklearn import datasets
from sklearn import linear_model

def on_key(event:mpl.backend_bases.KeyEvent):
    if event.key == 'escape':
        plt.close()

# data, target = datasets.make_regression(n_samples=100, n_features=1,
#     n_informative=1, n_targets=1, noise=10)
data, target = datasets.load_boston(True)
X = data
Y = target


# 定义图
w = tf.Variable(tf.random_uniform([X.shape[1]], -1.0, 1.0))
b = tf.Variable(tf.zeros([1]))
y = w * X + b

loss = tf.reduce_mean(tf.square(y - Y))
optimizer = tf.train.GradientDescentOptimizer(0.00005)
train = optimizer.minimize(loss)

init = tf.global_variables_initializer()

# 计算图
with tf.Session() as sess:
    sess.run(init)
    for step in range(200):
        sess.run(train)
        if step % 20 == 0:
            print(step, sess.run(w), sess.run(b))


fig = plt.figure('regression')
fig.canvas.mpl_connect('key_press_event', on_key)
ax = fig.add_subplot(111)
ax.scatter(X, Y)
# ax.plot(rgx, rgy, 'r-')
plt.show()
