import pandas as pd, numpy as np, matplotlib.pyplot as plt

data = pd.read_csv('ToyotaCorolla.csv')

x = data['KM']
y = data['Doors']
z = data['Price']

fig = plt.figure(figsize=(10, 6))

ax = plt.axes(projection='3d')
ax.scatter3D(x, y, z)
ax.set_title('3D Scatter Plot of Toyota Corolla Data')

plt.show()