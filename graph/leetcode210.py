# 210. Course Schedule II

from typing import List
def course(numCourses, prerequisites):
    graph = {i:[] for i in range(numCourses)}
    for a,b in prerequisites:
        graph[b].append(a)

    stack = [0] * numCourses
    result = []

    def dfs(node):
        if stack[node] == 1:
            return True
        if stack[node] == 2:
            return False
        stack[node] = 1

        for neig in graph[node]:
            if dfs(neig):
                return True
        
        stack[node] = 2
        result.append(node)
        return False

    for node in graph:
        if stack[node] == 0:
            if dfs(node):
                return []
            
    return result[::-1]

numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]

print(course(numCourses, prerequisites))