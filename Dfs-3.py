# Adjacency list representation of the graph
graph = {1: [2, 3], 2: [5, 6], 3: [4, 7], 4: [8], 5: [], 6: [], 7: [8], 8: []}

# Source node
start = 1

# DFS logic (using recursion)
visited = set()

def dfs(node):
    visited.add(node)
    print(node, end=" ")
    
    for neighbour in graph[node]:
        if neighbour not in visited:
            dfs(neighbour)

print("DFS Traversal:", end=" ")
dfs(start)
