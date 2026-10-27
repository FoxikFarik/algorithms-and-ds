import heapq

n = int(input())
prev, prevt = 0, 0
aquas = []
heapq.heapify(aquas)
for i in range(n):
    j = int(input())
    heapq.heappush(aquas, (max(1000-j, 1), i, j))

flag = True
while flag:
    t, pos, pop = aquas[0]
    if (t - prevt >= abs(pos - prev)):
        heapq.heapreplace(aquas, (t+max(1000-pop-1, 1), pos, pop+1))
        prevt, prev = t, pos
    else:
        flag = False

print(t)