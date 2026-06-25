import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.neighbors import KNeighborsClassifier

df = pd.read_csv("glass.csv")

X = df.drop('Type', axis=1).values
y = df['Type'].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

model = KNeighborsClassifier(n_neighbors=3, metric='euclidean')
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)

print("Confusion Matrix:")
print(cm)
print("Accuracy:", accuracy)

model = KNeighborsClassifier(n_neighbors=3, metric='manhattan')
model.fit(X_train, y_train)
y_pred = model.predict(X_test)  

accuracy = accuracy_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)

print("Confusion Matrix (Manhattan):")
print(cm)
print("Accuracy (Manhattan):", accuracy)