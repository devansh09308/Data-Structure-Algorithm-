from collections import deque
from typing import List

def eventualSafeNodes(graph: List[List[int]]) -> List[int]:
    n = len(graph)

    reverse_graph = [[] for _ in range(n)]
    outdegree = [0] * n

    # build reverse graph + outdegree
    for u in range(n):
        outdegree[u] = len(graph[u])
        for v in graph[u]:
            reverse_graph[v].append(u)   # reverse edge v <- u

    q = deque([i for i in range(n) if outdegree[i] == 0])

    while q:
        node = q.popleft()

        # node is safe, so its parents get "one less outgoing bad edge"
        for parent in reverse_graph[node]:
            outdegree[parent] -= 1
            if outdegree[parent] == 0:
                q.append(parent)

    # safe nodes are those whose outdegree became 0
    return [i for i in range(n) if outdegree[i] == 0]


graph = [
  [1,2],   # 0 -> 1,2
  [2,3],   # 1 -> 2,3
  [5],     # 2 -> 5
  [0],     # 3 -> 0
  [5],     # 4 -> 5
  [],      # 5 -> (none)
  []       # 6 -> (none)
]
