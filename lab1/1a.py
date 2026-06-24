import pandas as pd, numpy as np, matplotlib.pyplot as plt

data = pd.read_csv('ToyotaCorolla.csv')

data.head()

x = data['KM']
y = data['Price']

plt.figure(figsize=(10, 6))
plt.scatter(x, y, color='blue', alpha=0.5, s=10)

plt.xlabel('Kilometers Driven')
plt.ylabel('Price')
plt.title('Price vs Kilometers Driven')

plt.show()