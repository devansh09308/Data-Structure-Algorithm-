def has_cycle(graph):
    visited = set()

    def dfs(node, parent):
        if node not in visited:
            visited.add(node)

        for neighbour in graph[node]:
            if neighbour not in visited:
                if dfs(neighbour, node):
                    return True
            elif neighbour != parent:
                return True
        return False
            
    for node in graph:
        if node not in visited:
            if dfs(node, -1):
                return True
    return False

graph = {
    1: [2],
    2: [1, 3],
    3: [2, 4],
    4: [3, 1]
}


print(has_cycle(graph))