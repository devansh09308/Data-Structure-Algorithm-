def topoSortDFS(graph):
    visited = set()
    stack = []

    def dfs(node):
        visited.add(node)

        for neighbour in graph[node]:
            if neighbour not in visited:
                dfs(neighbour)

        stack.append(node)

    for node in graph:
        if node not in visited:
            dfs(node)

    return stack[::-1]



graph = {
    0: [1, 2],
    1: [3],
    2: [3],
    3: []
}
print(topoSortDFS(graph))