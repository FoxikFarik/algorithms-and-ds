N, S = map(int, input().split())
graph = []
visited = [False]*(N+1)

def dfs(v):
    global visited
    visited[v] = True
    
    for n in range(N):
        if  graph[v-1][n-1] == 1 and not visited[n]:
            dfs(n)

for _ in range(N):
    graph.append(list(map(int, input().split())))

dfs(S)
print(visited.count(True))
    