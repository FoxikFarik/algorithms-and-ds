from collections import deque

M, N = map(int, input().split())
graph = []
for _ in range(M):
    graph.append([i for i in input()])

moves = ((-1, 0), (1, 0),
        (0, -1), (0, 1))

visited = [[False for _ in range(N)] for _ in range(M)]
subgraphs = []
def bfs(i_0, j_0):
    visited[i_0][j_0] = True
    q = deque([(i_0, j_0)])

    while q:
        i, j = q.popleft()
        
        for di, dj in moves:
            ni = i + di
            nj = j + dj
            if 0 <= ni < M and 0 <= nj < N:
                if not visited[ni][nj] and graph[ni][nj] == '#':
                    visited[ni][nj] = True
                    q.append((ni, nj))

c = 0
for i in range(M):
    for j in range(N):
        if not visited[i][j] and graph[i][j] == '#':
            c += 1
            bfs(i, j)

print(c)