def hasCycle(graph):
    state = {node: 0 for node in graph}

    def dfs(node):
        if state[node] == 1:
            return True
        if state[node] == 2:
            return False
        state[node] = 1

        for neighbour in graph[node]:
            if dfs(neighbour):
                return True
        
        state[node] = 2
        return False

    for node in graph:
        if state[node] == 0:
            if dfs(node):
                return True
    
    return False

graph = {
  1: [2],
  2: [3],
  3: [4],
  4: [2]
}

print(hasCycle(graph))
