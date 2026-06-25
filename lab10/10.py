import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA

X = load_iris().data
y = load_iris().target

pca = PCA(n_components=2)
X_projected = pca.fit_transform(X)

plt.figure(figsize=(8, 6))
plt.scatter(X_projected[:, 0], X_projected[:, 1], c=y, cmap='jet')
plt.title('PCA of Iris Dataset')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.show()

lda = LDA(n_components=2)
X_projected_lda = lda.fit_transform(X, y)

plt.figure(figsize=(8, 6))
plt.scatter(X_projected_lda[:, 0], X_projected_lda[:, 1], c=y, cmap='jet')
plt.title('LDA of Iris Dataset')
plt.xlabel('Linear Discriminant 1')
plt.ylabel('Linear Discriminant 2')
plt.show()
