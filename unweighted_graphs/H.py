from collections import deque

INF = 1000

N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

S, F = map(int, input().split())
S, F = S-1, F-1
dist = [INF] * N
dist[S] = 0
pred = [-1] * N

q = deque([S])
while q:
    v = q.popleft()
    for i in range(N):
        if graph[v][i] == 1:
            if dist[i] > dist[v] + 1:
                dist[i] = dist[v] + 1
                pred[i] = v
                q.append(i)
                
path = [F]
ver = pred[F]
while ver != -1:
    path.append(ver)
    ver = pred[ver]
if path[-1] == S:
    print(dist[F])
    if dist[F] > 0:
        for v in path[::-1]:
            print(v+1, end=' ')
else:
    print(-1)