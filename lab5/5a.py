import pandas as pd, numpy as np, matplotlib.pyplot as plt

data = pd.read_csv('ToyotaCorolla.csv')

plt.title('Boxplot')
plt.boxplot(data['Price'], data=data['Price'], vert=False)
plt.xlabel('Price')
plt.show()