import pandas as pd, numpy as np, matplotlib.pyplot as plt

data = pd.read_csv('ToyotaCorolla.csv')

data.head()

x = data['KM']
y = data['Price']

plt.figure(figsize=(10, 6))
ax = plt.axes()
ax.scatter(x, y)
ax.set_title('Price vs Kilometers Driven')

plt.show()