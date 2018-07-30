
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn import linear_model
from sklearn import preprocessing

def on_key(event:mpl.backend_bases.KeyEvent):
    if event.key == 'escape':
        plt.close()

data, target = datasets.make_regression(n_samples=100, n_features=1,
    n_informative=1, n_targets=1, noise=10)
X = data
Y = target

# rg = linear_model.LinearRegression()        # 普通最小二乘法线性回归
rg = linear_model.Ridge(alpha=1.0)          # 岭回归，加入正则化
# rg = preprocessing.PolynomialFeatures(degree=3)
rg.fit(X, Y)
rgx = np.array([X.min() , X.max()])
rgy = rgx * rg.coef_.T + rg.intercept_

fig = plt.figure('regression')
fig.canvas.mpl_connect('key_press_event', on_key)
ax = fig.add_subplot(111)
ax.scatter(X, Y)
ax.plot(rgx, rgy, 'r-')
plt.show()
