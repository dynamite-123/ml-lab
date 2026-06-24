graph = {
    'A': [('B', 11), ('C', 14), ('D',7)],
    'B': [('A', 11), ('E', 15)],
    'C': [('A', 14), ('E', 8), ('D',18), ('F',10)],
    'D': [('A', 7), ('F', 25), ('C',18)],
    'E': [('B', 15), ('C', 8), ('H',9)],
    'F': [('G', 20), ('C', 10), ('D',25)],
    'G': [],
    'H': [('E',9), ('G',10)]
}

start = 'A'
goal = 'G'

heuristic = {
    'A': 40,
    'B': 32,
    'C': 25,
    'D': 35,
    'E': 19,
    'F': 17,
    'G': 0,
    'H': 10
}

from heapq import heappop, heappush


def bfs(graph, start, goal, heuristic):
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
                heappush(heap, (heuristic[nei], cost + nei_cost, nei, path + [nei]))

    return None


start = 'A'
goal = 'G'

result = bfs(graph, start, goal, heuristic)

if result:
    print(f"Minimum cost path from {start} to {goal} is {result[1]}")
    print(f"Cost: {result[0]}")
else:
    print(f"No path from {start} to {goal}")


