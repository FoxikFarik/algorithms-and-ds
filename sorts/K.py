n = int(input())

if n == 1:
    arr = [1]
else:
    arr = [1, 2]
    for i in range(3, n+1):
        arr.append(i)
        arr[i//2 - 1 + i % 2], arr[-1] = arr[-1], arr[i//2 - 1 + i % 2]
    
print(*arr)