n, m = map(int, input().split())
graph = {i: [] for i in range(1, n+1)}
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)

row = list(map(int, input().split()))
visited = set()
topo = True
for v in row:
    visited.add(v)
    for n in graph[v]:
        if n in visited:
            topo = False
            break

print('YES' if topo else 'NO')