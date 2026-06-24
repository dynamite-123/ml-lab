
def minimax(depth, node, is_maximizing_player, values):
    if depth == 0 or node > len(values) - 1:
        return values[node]
    
    if is_maximizing_player:
        best = float('-inf')
        for i in range(2):
            val = minimax(depth - 1, node * 2 + i, False, values)
            best = max(best, val)
        return best
    else:
        best = float('inf')
        for i in range(2):
            val = minimax(depth - 1, node * 2 + i, True, values)
            best = min(best, val)
        return best
    

values = [3, 5, 2, 9, 12, 5, 23, 23]

res = minimax(3, 0, True, values)
print(f"The optimal value is: {res}")
