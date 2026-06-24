# A* algorithm implementation
from heapq import heappop, heappush


def a_star(graph, start, goal, heuristic):
    heap = [(heuristic[start], 0, start, [start])]
    vis = set()

    while heap:
        _, cost, node, path = heappop(heap)

        if node == goal:
            return cost, path

        if node in vis:
            continue

        vis.add(node)
        for nei, nei_cost in graph[node]:
            if nei not in vis:
                heappush(heap, (cost + nei_cost + heuristic[nei], cost + nei_cost, nei, path + [nei]))

    return None


graph = {
    "A": [("B", 6), ("F", 3)],
    "B": [("C", 3), ("D", 2)],
    "C": [("D", 1), ("E", 5)],
    "D": [("C", 1), ("E", 8)],
    "E": [("I", 5), ("J", 5)],
    "F": [("G", 1), ("H", 7)],
    "G": [("I", 3)],
    "H": [("I", 2)],
    "I": [("E", 5), ("J", 3)],
}

heuristic = {
    "A": 10,
    "B": 8,
    "C": 5,
    "D": 7,
    "E": 3,
    "F": 6,
    "G": 5,
    "H": 3,
    "I": 1,
    "J": 0,
}

start = "A"
goal = "J"  

result = a_star(graph, start, goal, heuristic)

print(f"Minimum cost path from {start} to {goal} is {result[1]}")
print(f"Cost: {result[0]}")
