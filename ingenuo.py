import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.naive_bayes import GaussianNB
X, y = make_blobs(100, 2, centers=2, random_state=2, cluster_std=1.5)
plt.scatter(X[:, 0], X[:, 1], c=y, s=50, cmap='RdBu')
modelo = GaussianNB()
modelo.fit(X,y)
rng = np.random.RandomState(0)
Xnew = [-6, -14] + [14, 18] * rng.rand(2000, 2)
ynew = modelo.predict(Xnew)
plt.scatter(X[:,0], X[:,1], c=y, s=50, cmap='RdBu')
plt.scatter(X[:,0], X[:,1], c=y, s=50, cmap='RdBu')
lim = plt.axis()
plt.scatter(Xnew[:, 0], Xnew[:, 1], c=ynew, s=20, cmap='RdBu', alpha=0.5)# acá alpha da la trasparencia de los puntos
plt.axis(lim)

yprob = modelo.predict_proba(Xnew)
yprob[-18:].round(2)


plt.show()