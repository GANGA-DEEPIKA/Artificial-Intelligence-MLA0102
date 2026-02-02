from collections import deque

# Adjacency list of the graph
graph = {
    0: [1, 2],
    1: [3],
    2: [3],
    3: [4],
    4: [5],
    5: [6],
    6: [4]
}

start = 0

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
