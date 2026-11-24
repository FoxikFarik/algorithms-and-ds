from collections import deque

N, M = map(int, input().split())

graph = {i: [] for i in range(1, N+1)}
subgraphs = []
visited = [False]*(N+1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(start):
    visited[start] = True
    queue = deque([start])
    
    subgraph = []
    
    while queue:
        v = queue.popleft()
        subgraph.append(v)
        
        for n in graph[v]:
            if not visited[n]:
                visited[n] = True
                queue.append(n)
        
    return subgraph

for i in range(1, N+1):
    if not visited[i]:
        subgraphs.append(bfs(i))

print(len(subgraphs))
for subgraph in subgraphs:
    print(len(subgraph))
    print(*subgraph)
