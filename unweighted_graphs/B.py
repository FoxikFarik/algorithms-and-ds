n = int(input())
matr = []
for _ in range(n):
    matr.append(list(map(int, input().split())))
    
sources, drain = [], []
for i in range(n):
    if not(1 in matr[i]):
        drain.append(i+1)
    
    if not(1 in [matr[j][i] for j in range(n)]):
        sources.append(i+1)
        
print(len(sources))
for el in sources:
    print(el)
print(len(drain))
for el in drain:
    print(el)