def find_paths(graph, start, end, n):
    paths = []

    dfs(graph, start, end, n, [], paths)
    return paths

def dfs(graph, node, end, n, path, paths):
    path.append(node)

    if node == end and n == 0:
        paths.append(path[:])
    elif n > 0:
        for neighbor in graph[node]:
            dfs(graph, neighbor, end, n - 1, path[:], paths)

    path.pop()

def translate_transitions(paths):
    transitions = []
    for path in paths:
        transition = []
        for i in range(len(path)-1):
            transition.append(f"{path[i]}->{path[i+1]}")
        transitions.append(transition)
    return transitions