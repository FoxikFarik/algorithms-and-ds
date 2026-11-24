from sys import setrecursionlimit

N = int(input())
graph = []
color = ['white'] * N
cycle = 0

for _ in range(N):
    graph.append(list(map(int, input().split())))

def dfs(v):
    color[v] = 'gray'
    global cycle
    
    for i in range(N):
        if graph[v][i] == 1:
            if color[i] == 'gray':
                cycle = 1
            elif color[i] == 'white':
                dfs(i)
    
    color[v] = 'black'
    
for i in range(N):
    dfs(i)
    if cycle:
        break

print(cycle)