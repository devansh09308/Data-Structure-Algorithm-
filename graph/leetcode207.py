from typing import List

def course_schedule(numCourses, prerequisites):
    graph = {i: [] for i in range(numCourses)}
    for a, b in prerequisites:
        graph[b].append(a)

    state = [0] * numCourses

    def dfs(node):
        if state[node] == 1:
            return True

        if state[node] == 2:
            return False
        
        state[node] = 1

        for neig in graph[node]:
            if dfs(neig):
                return True
            
        state[node] = 2
        return False
    
    for course in range(numCourses):
        if state[course] == 0:
            if dfs(course):
                return False
            
    return True

numCourses = 2
prerequisites = [[1,0]]

print(course_schedule(numCourses, prerequisites))