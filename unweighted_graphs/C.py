n, m = map(int, input().split())
unique_pairs = 0
pairs = set()
for _ in range(m):
    o, i = map(int, input().split())
    if o > i:
        o, i = i, o
    if not((o, i) in pairs):
        pairs.add((o, i))
        unique_pairs += 1

print('YES' if unique_pairs == n*(n-1)//2 else 'NO')