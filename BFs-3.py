from collections import deque

# Adjacency list representation of the graph
graph = {1: [2, 3], 2: [5, 6], 3: [4, 7], 4: [8], 5: [], 6: [], 7: [8], 8: []}

# Source node
start = 1  # Use integer, not string

# BFS logic
visited = set([start])
queue = deque([start])

print("BFS Traversal:", end=" ")

while queue:
    node = queue.popleft()
    print(node, end=" ")

    for neighbour in graph[node]:
        if neighbour not in visited:
            visited.add(neighbour)
            queue.append(neighbour)
