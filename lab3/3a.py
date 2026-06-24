import pandas as pd, numpy as np, matplotlib.pyplot as plt

data = pd.read_csv('ToyotaCorolla.csv')

x = data['KM']
y = data['Price']
z = data['Weight']

plt.figure(figsize=(10, 6))
ax = plt.axes()
filled = ax.tricontourf(x, y, z, levels=15, cmap='jet')
plt.colorbar(filled, ax=ax)
ax.set_xlabel('KM')
ax.set_ylabel('Price')
ax.set_title('Contour plot of Price vs KM and Weight')
plt.show()