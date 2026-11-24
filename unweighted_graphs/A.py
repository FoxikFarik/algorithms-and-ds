n = int(input())
matr = []
for _ in range(n):
    matr.append(list(map(int, input().split())))

oriented = False

for i in range(n):
    if matr[i][i] != 0:
        oriented = True
        break
    for j in range(i+1, n):
        if matr[i][j] != matr[j][i]:
            oriented = True
            break

if oriented:
    print('NO')
else:
    print('YES')