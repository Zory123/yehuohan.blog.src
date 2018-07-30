
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn import linear_model
from sklearn import preprocessing

def on_key(event:mpl.backend_bases.KeyEvent):
    if event.key == 'escape':
        plt.close()

data, target = datasets.make_classification(n_samples=100, n_features=2,
    n_informative=1, n_redundant=0, n_classes=2, n_clusters_per_class=1)
X = data
Y = target
color = ['g', 'y']
C = [color[k] for k in Y]

rg = linear_model.LogisticRegression()      # 对数几率回归
rg.fit(X, Y)
rgx = np.array([0.5, 0.5], dtype=np.float64)
print(color[int(rg.predict(rgx.reshape(1, -1)))])

fig = plt.figure('regression')
fig.canvas.mpl_connect('key_press_event', on_key)
ax = fig.add_subplot(111)
ax.scatter(X[:, 0], X[:, 1], c=C)
ax.scatter(rgx[0], rgx[1], c='r')
plt.show()
