def count_components(graph):
    visited = set()
    count = 0

    def dfs(node):
        visited.add(node)

        for neighbour in graph[node]:
            if neighbour not in visited:
                dfs(neighbour)

    for node in graph:
        if node not in visited:
            count += 1
            dfs(node)

    return count

graph = {
    1: [2],
    2: [1, 3],
    3: [2],
    4: []
}

print(count_components(graph))