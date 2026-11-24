N, M = map(int, input().split())
visited = [False] * (N+1)

graph = {i: [] for i in range(1, N+1)}
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    
output = []

def dfs(v):
    visited[v] = 1
    
    for n in graph[v]:
        if not visited[n]:
            output.append((v, n))
            dfs(n)
    
dfs(1)
for u, v in output:
    print(u, v)