import numpy as np

X = np.array([[0,0], [0,1], [1,0], [1,1]])

y_and = np.array([0, 0, 0, 1])
y_or  = np.array([0, 1, 1, 1])

def step(x):
    return 1 if x >= 0 else 0

def perceptron(X, y, lr=0.1, epochs=10):
    w = np.zeros(X.shape[1])
    b = 0

    for _ in range(epochs):
        for xi, yi in zip(X, y):
            pred = step(np.dot(w, xi) + b)
            w += lr * (yi - pred) * xi
            b += lr * (yi - pred)

    return w, b

def print_results(name, X, y, w, b):
    print(f"\n--- {name} ---")
    print(" A  B | Target | Output")
    for xi, yi in zip(X, y):
        out = step(np.dot(w, xi) + b)
        print(f" {xi[0]}  {xi[1]} |   {yi}    |   {out}")

        
w, b = perceptron(X, y_and)
print_results("AND", X, y_and, w, b)
print(f"Weights: {w}, Bias: {b}")

w, b = perceptron(X, y_or)
print_results("OR", X, y_or, w, b)
print(f"Weights: {w}, Bias: {b}")