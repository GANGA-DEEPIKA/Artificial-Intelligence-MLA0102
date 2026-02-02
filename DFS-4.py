graph = {
    0: [1],
    1: [3],
    2: [1],
    3: [4, 2],  # neighbor order changed for desired DFS output
    4: [5],
    5: [7],
    6: [4],
    7: [6]
}

visited = set()

def dfs(node):
    visited.add(node)
    print(node, end=" ")
    for neighbour in graph.get(node, []):
        if neighbour not in visited:
            dfs(neighbour)

print("DFS Traversal:", end=" ")
# Loop through all nodes to cover disconnected components
for node in graph:
    if node not in visited:
        dfs(node)
