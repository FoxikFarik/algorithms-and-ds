def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    midel = arr[len(arr)//2+1]
    larr = []
    rarr = []
    for i in range(len(arr)):
        if i == len(arr)//2+1: continue
        if arr[i] < midel:
            larr.append(arr[i])
        else:
            rarr.append(arr[i])
    larr = quick_sort(larr)
    rarr = quick_sort(rarr)
    larr.append(midel)
    larr.extend(rarr)
    
    return larr

N = int(input())
arr = list(map(int, input().split()))
arr = quick_sort(arr)
print(*arr)
    