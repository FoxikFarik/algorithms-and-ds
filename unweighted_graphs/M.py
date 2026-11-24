n, m = map(int, input().split())
graph = {i: [] for i in range(1, n+1)}
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

types = [0]*(n+1)
ans = True

def dfs(v):
    global ans
    if not types[v]:
        types[v] = 1
    
    for n in graph[v]:
        if types[v] == types[n]:
            ans = False
            return
        elif types[n] == 0:
            if types[v] == 1:
                types[n] = 2
            else:
                types[n] = 1
            dfs(n)

for i in range(1, n+1):
    if ans:
        dfs(i)
if ans:
    print('YES')
    for i in range(1, n+1):
        if types[i] == 1:
            print(i, end=' ')
else:
    print('NO')