import random

def foo(x):
    return -(x**2)

def hill_climbing(start, delta=1, max_iterations=1000):
    cur = start
    for _ in range(max_iterations):
        neighbors = [cur + delta, cur - delta]
        next_move = max(neighbors, key=foo)
        if foo(next_move) <= foo(cur):
            break
        cur = next_move
    return cur

start = random.randint(-10, 10)
best_x = hill_climbing(start)
best_y = foo(best_x)

print(f"Best x: {best_x}\nBest y: {best_y}")