import heapq

n = int(input())
packages = []
for _ in range(n):
    T, L = map(int, input().split())
    packages.append((T, L))

packages.sort()
check = []
heapq.heapify(check)
max_size = 0
for time, dur in packages:
    heapq.heappush(check, time + dur)
    while (check[0] <= time):
        heapq.heappop(check)
    max_size = max(max_size, len(check))

print(max_size)