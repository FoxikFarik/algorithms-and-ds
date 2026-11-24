from collections import deque

INF = 1000

N = int(input())
graph = dict()
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())

S = (x1, y1)
F = (x2, y2)
moves = ((-2, -1), (-2, 1),
         (2, -1), (2, 1),
         (-1, -2), (-1, 2),
         (1, -2), (1, 2))


visited = {S}
pred = {S: None}
q = deque([S])
while q:
    x, y = q.popleft()
    
    if (x, y) == F:
        break
    
    for dx, dy in moves:
        nx = x + dx
        ny = y + dy
        
        if 1 <= nx <= N and 1 <= ny <= N:
            if (nx, ny) not in visited:
                visited.add((nx, ny))
                pred[(nx, ny)] = (x, y)
                q.append((nx, ny))


path = [F]
ver = pred[F]
while ver != None:
    path.append(ver)
    ver = pred[ver]

print(len(path) - 1)
for x, y in path[::-1]:
    print(x, y)