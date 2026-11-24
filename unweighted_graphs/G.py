from sys import setrecursionlimit

N, M = map(int, input().split())
graph = {i: [] for i in range(1, N+1)}
color = [0] + ['white'] * N
cycle = False

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(v, prev):
    color[v] = 'gray'
    global cycle
    
    for n in graph[v]:
        if n == prev:
            continue
        if color[n] == 'gray':
            cycle = True
        elif color[n] == 'white':
            dfs(n, v)
    
    color[v] = 'black'
    
dfs(1, None)
if cycle or 'white' in color:
    print("NO")
else:
    print("YES")