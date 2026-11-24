from collections import deque

N, M = map(int, input().split())
labirynth = []
for _ in range(N):
    labirynth.append(list(map(int, input().split())))
    
dist = [[-1 for _ in range(M)] for _ in range(N)]
S = (0, 0)
F = (N-1, M-1)
moves = ((-1, 0), (1, 0),
         (0, -1), (0, 1))

q = deque([S])
dist[0][0] = 0
while q:
    row, col = q.popleft()
    
    for drow, dcol in moves:
        nrow = row + drow
        ncol = col + dcol
        if 0 <= nrow < N and 0 <= ncol < M:
            if labirynth[nrow][ncol] == 0 and dist[nrow][ncol] == -1:
                dist[nrow][ncol] = dist[row][col] + 1
                q.append((nrow, ncol))
    
print(dist[F[0]][F[1]])
