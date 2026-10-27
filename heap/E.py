import heapq

N = int(input())
H = list(map(int, input().split()))
ans = 0
heapq.heapify(H)
while len(H) > 1:
    c = heapq.heappop(H) + heapq.heappop(H)
    ans += c * 0.05
    heapq.heappush(H, c)

print(f'{ans:.2f}')