Minimax(node, depth, isMaximizingPlayer):
    if node is a leaf or depth == 0:
        return value of node

    if isMaximizingPlayer:
        bestValue ← -infinity
        for each childNode of node:
            value ← Minimax(childNode, depth-1, False)
            bestValue ← max(bestValue, value)
        return bestValue

    else:  # Minimizing Player
        bestValue ← +infinity
        for each childNode of node:
            value ← Minimax(childNode, depth-1, True)
            bestValue ← min(bestValue, value)
        return bestValue
