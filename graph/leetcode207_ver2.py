from typing import List
from collections import deque

def course_schedule(numCourses, prerequisites):
    graph = {i: [] for i in range(numCourses)}
    indegree = [0] * numCourses


    for a, b in prerequisites:
        graph[b].append(a)
        indegree[a] += 1

    taken = 0

    q = deque(i for i in range(numCourses) if indegree[i] == 0)

    while q:
        course = q.popleft()
        taken += 1

        for neig in graph[course]:
            indegree[neig] -= 1
            if indegree[neig] == 0:
                q.append(neig)

    return taken == numCourses

numCourses = 2
prerequisites = [[1,0]]

print(course_schedule(numCourses, prerequisites))