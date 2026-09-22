from collections import deque
import timeit

# Small graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H'],
    'E': ['I'],
    'F': ['J'],
    'G': ['K'],
    'H': [],
    'I': [],
    'J': [],
    'K': []
}


# BFS function
def bfs(graph, start, goal):
    queue = deque([(start, [start])])
    visited = set()
    nodes_expanded = 0

    while queue:
        node, path = queue.popleft()

        if node in visited:
            continue

        visited.add(node)
        nodes_expanded += 1

        if node == goal:
            return path, nodes_expanded

        for neighbour in graph[node]:
            if neighbour not in visited:
                queue.append((neighbour, path + [neighbour]))

    return None, nodes_expanded


# DFS function
def dfs(graph, start, goal):
    stack = [(start, [start])]
    visited = set()
    nodes_expanded = 0

    while stack:
        node, path = stack.pop()

        if node in visited:
            continue

        visited.add(node)
        nodes_expanded += 1

        if node == goal:
            return path, nodes_expanded

        for neighbour in reversed(graph[node]):
            if neighbour not in visited:
                stack.append((neighbour, path + [neighbour]))

    return None, nodes_expanded


# Run BFS
bfs_path, bfs_nodes = bfs(graph, 'A', 'K')

# Run DFS
dfs_path, dfs_nodes = dfs(graph, 'A', 'K')


# Measure execution time
bfs_time = timeit.timeit(
    lambda: bfs(graph, 'A', 'K'),
    number=10000
)

dfs_time = timeit.timeit(
    lambda: dfs(graph, 'A', 'K'),
    number=10000
)


# Average time in milliseconds
bfs_avg_ms = (bfs_time / 10000) * 1000
dfs_avg_ms = (dfs_time / 10000) * 1000


# Display results
print("=" * 45)
print("       SLE-2 BFS vs DFS PROFILING")
print("=" * 45)

print("\nBFS RESULTS")
print("Path:", bfs_path)
print("Nodes Expanded:", bfs_nodes)
print("Average Time:", round(bfs_avg_ms, 6), "ms")

print("\nDFS RESULTS")
print("Path:", dfs_path)
print("Nodes Expanded:", dfs_nodes)
print("Average Time:", round(dfs_avg_ms, 6), "ms")

print("\n" + "=" * 45)
print("COMPARISON")
print("=" * 45)

if bfs_avg_ms < dfs_avg_ms:
    print("BFS has lower execution time.")
elif dfs_avg_ms < bfs_avg_ms:
    print("DFS has lower execution time.")
else:
    print("Both have almost equal execution time.")

if bfs_nodes < dfs_nodes:
    print("BFS expanded fewer nodes.")
elif dfs_nodes < bfs_nodes:
    print("DFS expanded fewer nodes.")
else:
    print("Both expanded the same number of nodes.")